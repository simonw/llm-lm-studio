import httpx
import llm
from llm.default_plugins.openai_models import Chat, AsyncChat
import os


def prepare(model_details, **kwargs):
    model_name = model_details["id"]
    model_id = f"lm-studio/{model_name}"
    kwargs["vision"] = model_details["type"] == "vlm"
    kwargs["supports_tools"] = "tool_use" in model_details.get("capabilities", [])
    kwargs.update(
        model_name=model_name,
        model_id=model_id,
        api_base="http://localhost:1234/v1",
    )
    return model_id, kwargs


class LMStudio(Chat):
    key = "sk-lm-studio"

    def __init__(self, model_details, **kwargs):
        self.model_id, kwargs = prepare(model_details, **kwargs)
        super().__init__(**kwargs)

    def __str__(self):
        return "lm-studio: {}".format(self.model_id)


class AsyncLMStudio(AsyncChat):
    key = "sk-lm-studio"

    def __init__(self, model_details, **kwargs):
        self.model_id, kwargs = prepare(model_details, **kwargs)
        super().__init__(**kwargs)

    def __str__(self):
        return f"lm-studio (async): {self.model_id}"


@llm.hookimpl
def register_models(register):
    try:
        response = httpx.get("http://localhost:1234/api/v0/models", timeout=0.1)
    except httpx.HTTPError:
        return
    for model_details in response.json()["data"]:
        # {
        #     "id": "mistral-small-3.2-24b-instruct-2506",
        #     "object": "model",
        #     "type": "vlm",
        #     "publisher": "lmstudio-community",
        #     "arch": "llama",
        #     "compatibility_type": "gguf",
        #     "quantization": "Q4_K_M",
        #     "state": "loaded",
        #     "max_context_length": 131072,
        #     "loaded_context_length": 4096
        # }
        if model_details["type"] in ("llm", "vlm"):
            register(LMStudio(model_details), AsyncLMStudio(model_details))
        # TODO: handle type of "embeddings"
