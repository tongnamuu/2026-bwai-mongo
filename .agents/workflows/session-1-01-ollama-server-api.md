---
description: Session 1 01 Ollama Server API
---

# Session 1 01 Ollama Server API

Python 초보자용 핸즈온 코드를 생성하세요. 추가 질문을 하지 말고 바로 작업하세요.

목표는 로컬 Ollama 서버 API로 Gemma 4를 호출하는 Python 파일 하나를 만드는 것입니다. Ollama CLI를 직접 호출하는 예제는 만들지 마세요.

생성할 파일:

```text
hands-on/session-1/work/01_ollama_server_api.py
hands-on/session-1/work/.env.example
```

전제:

- `hands-on/session-1/work/pyproject.toml`은 실습용으로 이미 제공되어 있습니다.
- 필요하면 `hands-on/session-1/work`에서 `uv sync`를 실행합니다.
- `ollama pull gemma4:e2b`를 이미 실행했거나 행사 전에 모델을 다운로드한 상태입니다.
- Python 파일에 PEP 723 inline script metadata를 넣지 마세요.
- 실행 방식은 `uv run python 01_ollama_server_api.py`입니다.

코드 요구사항:

- Python 3.10 이상 기준으로 작성하세요.
- `argparse`를 사용하세요.
- `.env` 파일을 `python-dotenv`의 `load_dotenv()`로 읽으세요.
- HTTP 클라이언트는 `httpx`를 사용하세요.
- 기본 호스트는 `http://localhost:11434`입니다.
- 호스트는 `--host` 옵션 또는 `OLLAMA_HOST` 환경 변수로 바꿀 수 있게 하세요.
- 기본 모델은 `gemma4:e2b`입니다.
- 모델은 `--model` 옵션 또는 `OLLAMA_MODEL` 환경 변수로 바꿀 수 있게 하세요.
- `--prompt` 옵션을 제공하세요.
- `--system` 옵션을 제공하세요.
- `--endpoint` 옵션을 제공하고 값은 `ollama` 또는 `openai`만 허용하세요.
- 기본 엔드포인트는 `ollama`입니다.
- 생성 전에 `GET /api/tags`로 Ollama 서버 연결과 모델 존재 여부를 확인하세요.
- `--endpoint ollama`는 `POST /api/chat`을 사용하세요.
- `--endpoint openai`는 `POST /v1/chat/completions`를 사용하세요.
- 스트리밍이 아닌 응답을 사용하세요.
- system message와 user message를 모두 포함하세요.
- 서버 연결 실패, 모델 미다운로드, API 호출 실패는 한국어로 안내하세요.
- 출력에는 호스트, 엔드포인트, 모델명, 프롬프트, 응답 텍스트가 잘 보이게 하세요.
- 코드는 초보자가 읽기 쉽도록 짧게 유지하세요.
- `.env.example`에는 `OLLAMA_HOST`, `OLLAMA_API_BASE`, `OLLAMA_MODEL`, `ADK_OLLAMA_MODEL` 예시만 넣으세요.

생성 후 가능하면 다음 검사를 실행하세요.

```bash
cd hands-on/session-1/work
uv run python -m py_compile 01_ollama_server_api.py
uv run python 01_ollama_server_api.py --help
```

Ollama 실제 생성 호출은 작은 장비에서는 시간이 걸릴 수 있으므로 명시적인 요청이 있을 때만 실행하세요.
