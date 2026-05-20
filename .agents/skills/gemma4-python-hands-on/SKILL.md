---
name: gemma4-python-hands-on
description: Guides Gemma 4 Python hands-on code generation and review for this repository. Use when creating, checking, or troubleshooting session 1 Python examples.
---

# Gemma 4 Python Hands-on

Use this skill for Session 1 Python hands-on tasks in this repository.

## Context

- The hands-on work directory is `hands-on/session-1/work/`.
- Shared rules live in `.agents/rules/session-1-common-rules.md`.
- Ollama server API code generation is described in `.agents/workflows/session-1-01-ollama-server-api.md`.
- ADK Ollama agent generation is described in `.agents/workflows/session-1-02-adk-ollama.md`.

## Guidance

1. Follow the shared Session 1 rules before generating or editing code.
2. Keep examples short, beginner-friendly, and Python 3.10+ compatible.
3. Use `uv run python <file>` for script execution examples and `uv run adk run <agent_package>` for ADK agents.
4. Use `python-dotenv` for `.env` loading, but do not create or print real secret values.
5. Prefer `httpx` for direct Ollama server API calls and `google-adk` for ADK agents.
6. For ADK Ollama agents, create a small `BaseLlm` adapter that calls Ollama `/api/chat` with `httpx`.
7. After generating code, check with `py_compile` and use `--help` for regular scripts when possible.
8. Do not run long Ollama generations unless the user explicitly asks.
