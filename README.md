# LangChain & LiteLLM Experiments

This folder contains small experimental scripts exploring simple integrations and usage patterns with LangChain-style flows and LiteLLM-style local models. Use these as starting points for experimentation, not production-ready code.

## Contents

- `exp_langchain.py` — experiments demonstrating simple LangChain patterns and prompt/response chaining.
- `exp_litellm.py` — experiments focused on integrating with LiteLLM or lightweight local LLMs.
- `exp_txt_read.py` — utilities/examples for reading and processing text files (uses `hamlet.txt`).
- `hamlet.txt` — sample text used by the text-processing experiments.
- `single_arg_llm_conv.py` — minimal example wrapping an LLM call that accepts a single input argument and returns a response.
- `two_arg_llm.py` — minimal example wrapping an LLM call that accepts two arguments (e.g., context + query) and returns a response.

## Prerequisites

- Python 3.8 or newer.
- Install any libraries you plan to use (examples below). Adjust according to the actual imports used in each script.

Example quick setup:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install langchain litellm requests
```

If you use OpenAI, Ollama, or another provider, set your API keys or local server endpoints in environment variables before running the scripts.

## Running the examples

- Run a LangChain experiment:

```bash
python exp_langchain.py
```

- Run the LiteLLM experiment:

```bash
python exp_litellm.py
```

- Read/process the sample text:

```bash
python exp_txt_read.py
```

- Try the LLM wrappers:

```bash
python single_arg_llm_conv.py
python two_arg_llm.py
```

## Notes

- Inspect each script for required imports and environment variables (API keys, endpoints). The example dependency list above is a guess — adjust to the actual packages used by the scripts.
- These scripts are intentionally minimal and intended for learning and prototyping.

## Next steps (suggested)

- Add a `requirements.txt` or `pyproject.toml` with exact dependencies.
- Add example config or `.env.example` showing required environment variables.
- Expand one script into a small demo that wires inputs, caching, and simple error handling.

---

If you want, I can: generate a `requirements.txt`, add runnable examples with mock inputs, or annotate each file with short inline comments. Which would you like next?
