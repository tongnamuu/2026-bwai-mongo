# Gemma 4 Python 핸즈온 생성 프롬프트

[메인 안내로 돌아가기](../README.md)

60분 실습용 Python 핸즈온 생성 프롬프트는 [`hands-on/session-1`](../hands-on/session-1)에 있습니다.

## 실습 흐름

| 순서 | 파일 | 내용 |
| --- | --- | --- |
| 1 | [`.agents/rules/rules.md`](../.agents/rules/rules.md) | Antigravity 공통 rule |
| 2 | [`.agents/rules/session-1-common-rules.md`](../.agents/rules/session-1-common-rules.md) | 수동 설정용 공통 rule 사본 |
| 3 | [`.agents/workflows/session-1-01-ollama-server-api.md`](../.agents/workflows/session-1-01-ollama-server-api.md) | Ollama 서버 API 예제 생성 workflow |
| 4 | [`.agents/workflows/session-1-02-adk-ollama.md`](../.agents/workflows/session-1-02-adk-ollama.md) | ADK Ollama agent 생성 workflow |
| 5 | [`.agents/skills/gemma4-python-hands-on/SKILL.md`](../.agents/skills/gemma4-python-hands-on/SKILL.md) | Session 1 Python 핸즈온 skill |
| 6 | [`prompts/01-ollama-server-api-system-prompt.md`](../hands-on/session-1/prompts/01-ollama-server-api-system-prompt.md) | AI Studio용 Ollama 서버 API 시스템 프롬프트 |
| 7 | [`prompts/02-adk-ollama-system-prompt.md`](../hands-on/session-1/prompts/02-adk-ollama-system-prompt.md) | AI Studio용 ADK Ollama 시스템 프롬프트 |
| 8 | [`work/pyproject.toml`](../hands-on/session-1/work/pyproject.toml) | 실습용 uv 프로젝트 설정 |
| 9 | [`reference/`](../hands-on/session-1/reference) | 참고 구현 |

## Antigravity에서 실행

Antigravity를 사용할 경우 이 저장소 루트를 열거나 Antigravity 2.0 Project에 추가하고, Agent 패널의 Customizations에서 rules, workflows, skills가 보이는지 확인합니다. 설정 위치와 수동 추가 방법은 [Google Antigravity 2.0 및 CLI 준비 가이드](./07-google-antigravity.md)에 정리되어 있습니다.

### Skills 활용 방식

이 핸즈온에서 workflow는 `/session-1-01-ollama-server-api`처럼 실행할 절차를 담당하고, skill은 Agent가 Session 1 Python 실습의 배경 지식과 검토 기준을 참고하게 하는 역할입니다.

저장소 skill 위치:

```text
.agents/skills/gemma4-python-hands-on/SKILL.md
```

Agent가 자동으로 skill을 참고하지 않는 것처럼 보이면 요청에 skill 이름을 직접 넣어 주세요.

```text
gemma4-python-hands-on skill을 참고해서 Session 1 규칙에 맞게 코드를 생성해 줘.
```

생성 이후 검토나 문제 해결에도 같은 skill을 사용할 수 있습니다.

```text
gemma4-python-hands-on skill 기준으로 hands-on/session-1/work/01_ollama_server_api.py를 검토하고 필요한 부분만 고쳐 줘.
```

Agent 입력창에서 다음 workflow를 실행합니다.

```text
/session-1-01-ollama-server-api
/session-1-02-adk-ollama
```

Workflow가 자동으로 보이지 않으면 `.agents/workflows/`의 Markdown 파일 내용을 프로젝트 또는 Workspace workflow로 직접 추가하세요. Antigravity를 쓰지 않는 경우에는 `hands-on/session-1/prompts/`의 시스템 프롬프트를 AI Studio 등에 붙여넣어 같은 실습 코드를 만들 수 있습니다.

## 가장 짧은 준비와 실행 명령

`uv`가 설치되어 있지 않다면 먼저 [Python + uv 설치 가이드](./09-python-uv-setup.md)를 확인하세요.

`work/`에는 실습용 `pyproject.toml`이 이미 들어 있습니다. 패키지를 미리 설치하려면 다음만 실행합니다.

```bash
cd hands-on/session-1/work
uv sync
```

각 Antigravity workflow 또는 AI Studio용 시스템 프롬프트로 코드 생성 후 실행합니다.

Ollama 서버 설정은 생성된 `.env.example`을 `.env`로 복사해 확인하는 방식을 권장합니다.

01 Ollama 서버 API:

```bash
ollama pull gemma4:e2b
ollama serve
uv run python 01_ollama_server_api.py
```

02 ADK Ollama:

```bash
export OLLAMA_API_BASE=http://localhost:11434
uv run adk run adk_02_ollama_agent
```

02 ADK Ollama 예제는 `httpx`로 Ollama `/api/chat`을 직접 호출하는 작은 ADK custom model adapter를 사용합니다.

자세한 진행 순서와 옵션은 [`hands-on/session-1/README.md`](../hands-on/session-1/README.md)를 확인하세요.
