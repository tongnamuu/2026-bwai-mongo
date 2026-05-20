---
description: Session 1 02 ADK Ollama
---

# Session 1 02 ADK Ollama

Python 초보자용 ADK 핸즈온 코드를 생성하세요. 추가 질문을 하지 말고 바로 작업하세요.

목표는 Google ADK의 `LlmAgent`가 작은 `BaseLlm` custom adapter를 통해 로컬 Ollama 서버의 Gemma 4를 호출하는 최소 에이전트 패키지를 만드는 것입니다. Ollama CLI를 직접 호출하는 예제는 만들지 마세요.

생성할 파일:

```text
hands-on/session-1/work/adk_02_ollama_agent/__init__.py
hands-on/session-1/work/adk_02_ollama_agent/agent.py
```

전제:

- `hands-on/session-1/work/pyproject.toml`은 실습용으로 이미 제공되어 있습니다.
- 필요하면 `hands-on/session-1/work`에서 `uv sync`를 실행합니다.
- `ollama pull gemma4:e2b`를 이미 실행했거나 행사 전에 모델을 다운로드한 상태입니다.
- Ollama 앱을 실행했거나 별도 터미널에서 `ollama serve`를 실행한 상태입니다.
- Python 파일에 PEP 723 inline script metadata를 넣지 마세요.
- 실행 방식은 `uv run adk run adk_02_ollama_agent`입니다.

코드 요구사항:

- Python 3.10 이상 기준으로 작성하세요.
- ADK agent package 구조를 사용하세요.
- `__init__.py`는 `from . import agent`만 포함하세요.
- `.env` 파일을 `python-dotenv`의 `load_dotenv()`로 읽으세요.
- `.env`는 현재 agent 폴더의 부모 폴더와 현재 작업 디렉터리 양쪽에서 읽을 수 있게 하세요.
- `from google.adk.agents import LlmAgent`를 사용하세요.
- `from google.adk.models import BaseLlm, LlmRequest, LlmResponse`를 사용하세요.
- `from google.genai import types`를 사용하세요.
- `httpx.AsyncClient`로 Ollama native `/api/chat` 엔드포인트를 직접 호출하는 작은 `OllamaChatLlm(BaseLlm)` 클래스를 작성하세요.
- 외부 모델 라우팅 라이브러리나 별도 모델 래퍼를 추가하지 마세요.
- 기본 Ollama API base는 `http://localhost:11434`입니다.
- API base는 `OLLAMA_API_BASE` 환경 변수를 우선 사용하고, 없으면 `OLLAMA_HOST` 환경 변수, 그것도 없으면 기본값을 사용하세요.
- 기본 모델은 `gemma4:e2b`입니다.
- 모델은 `ADK_OLLAMA_MODEL` 또는 `OLLAMA_MODEL` 환경 변수로 바꿀 수 있게 하세요.
- `model=OllamaChatLlm(model=model_tag, api_base=api_base)` 형태로 모델을 연결하세요.
- `root_agent = LlmAgent(...)`를 모듈 최상위에 정의하세요.
- agent 이름은 `adk_ollama_gemma4_agent`로 하세요.
- instruction은 한국어 답변, numbered steps, 로컬 모델 실습 친화적 설명을 요구하도록 작성하세요.
- 이 실습은 먼저 ADK-Ollama 연결을 확인하는 것이 목표이므로 custom tools는 추가하지 마세요.
- 코드는 초보자가 읽기 쉽도록 짧게 유지하세요.

생성 후 가능하면 다음 검사를 실행하세요.

```bash
cd hands-on/session-1/work
uv run python -m py_compile adk_02_ollama_agent/agent.py
```

Ollama 실제 생성 호출은 작은 장비에서는 시간이 걸릴 수 있으므로 명시적인 요청이 있을 때만 실행하세요.
