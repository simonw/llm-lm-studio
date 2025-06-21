# llm-lm-studio

[![PyPI](https://img.shields.io/pypi/v/llm-lm-studio.svg)](https://pypi.org/project/llm-lm-studio/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-lm-studio?include_prereleases&label=changelog)](https://github.com/simonw/llm-lm-studio/releases)
[![Tests](https://github.com/simonw/llm-lm-studio/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/llm-lm-studio/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-lm-studio/blob/main/LICENSE)

LLM plugin for local models via [LM Studio](https://lmstudio.ai/)

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-lm-studio
```
## Usage

Run this command to see the list of available models:

```bash
llm models -q lm-studio
```
Run models using their model ID, for example:
```bash
llm -m lmstudio/llama-3.2-3b-instruct 'say hi in five languages'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-lm-studio
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
