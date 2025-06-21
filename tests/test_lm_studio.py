import llm


def test_models_are_available(httpx_mock):
    httpx_mock.add_response(
        "http://localhost:1234/api/v0/models",
        json={
            "data": [
                {
                    "id": "mistralai/mistral-small-3.2",
                    "object": "model",
                    "type": "vlm",
                    "publisher": "mistralai",
                    "arch": "llama",
                    "compatibility_type": "gguf",
                    "quantization": "Q4_K_M",
                    "state": "loaded",
                    "max_context_length": 131072,
                    "loaded_context_length": 4096,
                },
                {
                    "id": "llama-3.2-3b-instruct",
                    "object": "model",
                    "type": "llm",
                    "publisher": "mlx-community",
                    "arch": "llama",
                    "compatibility_type": "mlx",
                    "quantization": "4bit",
                    "state": "loaded",
                    "max_context_length": 131072,
                    "loaded_context_length": 4096,
                    "capabilities": ["tool_use"],
                },
            ]
        },
        is_reusable=True,
    )
    model_ids = [model.model_id for model in llm.get_models()]
    assert "lm-studio/mistralai/mistral-small-3.2" in model_ids
    assert "lm-studio/llama-3.2-3b-instruct" in model_ids
    # llama-3.2-3b-instruct should support tools, not vision
    model1 = llm.get_model("lm-studio/llama-3.2-3b-instruct")
    assert not model1.vision
    assert model1.supports_tools
    # mistralai/mistral-small-3.2 supports vision, not tools
    model2 = llm.get_model("lm-studio/mistralai/mistral-small-3.2")
    assert model2.vision
    assert not model2.supports_tools
