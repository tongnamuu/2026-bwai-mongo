# Session 1 사전 준비 가이드

Ollama와 Gemma 4 모델, Python, `uv`를 행사 전에 준비합니다.

행사 당일에 처음 Ollama, `uv`, Python 패키지, Gemma 4 모델을 다운로드하는 방식은 피하는 것이 좋습니다. Gemma 4 모델은 작은 모델도 수 GB라서, 현장 네트워크 상태에 따라 다운로드에 시간이 오래 걸릴 수 있습니다. 행사 전까지 다음 항목을 마쳐 주세요.

1. Ollama 설치 완료
2. Gemma 4 모델 다운로드 완료
3. 터미널 실행 테스트와 API 테스트 1회 성공
4. Python + `uv` 설치와 Session 1 `work/` 프로젝트 동기화 테스트 성공
5. 코드 편집기를 사용할 경우 Antigravity IDE 또는 기존 편집기 실행 확인
6. Antigravity 2.0을 사용할 경우 Project 생성과 행사 자료 폴더 연결 확인
7. Antigravity CLI를 사용할 경우 `agy --version`과 첫 로그인 확인
8. Antigravity 설정을 사용할 경우 rules, workflows, skills 위치 확인

## 대상

이 문서는 Ollama로 로컬 LLM 서버와 API를 준비하는 다음 환경을 대상으로 합니다.

- Windows 노트북
- macOS Apple Silicon Mac
- macOS Intel Mac

Linux, ChromeOS, LM Studio, llama.cpp 같은 다른 로컬 LLM 실행 경로는 이 문서의 범위에서 제외합니다.
코드 편집기와 에이전트 도구는 Google Antigravity를 선택 준비 항목으로 다룹니다.

## 준비 요약

- 사전 설치 소프트웨어는 아래 표를 기준으로 준비합니다.
- 이번 행사 기본 모델은 `gemma4:e4b`입니다.
- 8GB 메모리 장비는 운영체제와 관계없이 `gemma4:e2b`만 준비하는 것을 권장합니다.
- Intel Mac은 Ollama 공식 macOS 지원 기준에서 CPU 전용입니다. Mac에 GPU가 없다는 뜻은 아니지만, 16GB 이상이면 `gemma4:e4b`를 준비하고 8GB 장비만 `gemma4:e2b`를 준비하세요.
- `gemma4:latest`는 나중에 바뀔 수 있으므로 행사 준비에서는 명시적 태그를 쓰세요.
- Ollama 서버 기본 주소는 `http://localhost:11434`입니다.
- Python 핸즈온을 진행하려면 [Python + uv 설치 가이드](../../docs/09-python-uv-setup.md)를 먼저 확인하세요.
- Session 1의 `hands-on/session-1/work/pyproject.toml`은 미리 제공되므로, `uv init` 대신 `uv sync` 또는 `uv run`으로 시작하면 됩니다.
- 코드 편집기나 에이전트 도구가 필요하면 [Google Antigravity 2.0 및 CLI 준비 가이드](../../docs/07-google-antigravity.md)를 확인하세요.
- 60분 실습용 Python 생성 프롬프트는 [Gemma 4 Python 핸즈온 생성 프롬프트](../../docs/08-python-hands-on.md)를 확인하세요.

## 사전 설치 소프트웨어

| 구분 | 소프트웨어 | 확인 명령 또는 기준 |
| --- | --- | --- |
| 필수 | Ollama | `ollama --version` |
| 필수 | Gemma 4 모델 | `ollama list`에서 `gemma4:e4b` 확인. 8GB 장비는 `gemma4:e2b` |
| 필수 | `uv` | `uv --version` |
| 필수 | Python 3.10 이상 | `uv run python --version` |
| 선택 | Antigravity IDE 또는 기존 코드 편집기 | 행사 자료 폴더 열기 |
| 선택 | Antigravity CLI | `agy --version`과 첫 로그인 확인 |

Antigravity는 Ollama와 Python 코드 실행 자체에는 필수는 아닙니다. 다만 에이전트 기반 코드 생성 흐름을 그대로 따라가려면 Antigravity IDE 또는 Antigravity CLI 중 하나를 행사 전에 실행해 두는 것을 권장합니다.

## Ollama 개요

Ollama는 로컬 컴퓨터에서 LLM을 다운로드하고 실행하는 도구입니다. 설치하면 터미널에서 `ollama run`, `ollama pull` 같은 명령을 사용할 수 있고, 로컬 API 서버는 기본적으로 `http://localhost:11434`에서 동작합니다.

이번 행사에서는 Ollama를 다음 용도로 사용합니다.

- Gemma 4 모델을 내 노트북에 미리 다운로드
- 인터넷 없이도 로컬에서 모델 실행
- 터미널에서 간단한 대화 테스트
- 로컬 API 서버를 통해 앱, 스크립트, 에이전트 도구와 연결

자세한 설명은 [Ollama와 Gemma 4 개요](../../docs/01-ollama-gemma4-overview.md)에 정리되어 있습니다.

## Gemma 4 개요

Gemma 4는 Google DeepMind가 공개한 오픈 모델 계열입니다. Google 공식 블로그는 Gemma 4가 고급 추론, 에이전트형 워크플로우, 코드 생성, 멀티모달 입력, 긴 컨텍스트를 목표로 설계됐다고 설명합니다.

이번 행사에서는 Ollama에서 바로 실행 가능한 다음 태그를 기준으로 준비합니다.

| 모델 | Ollama 태그 | 표시 크기 | 컨텍스트 | 권장 환경 |
| --- | --- | ---: | ---: | --- |
| Gemma 4 E4B | `gemma4:e4b` | 9.6GB | 128K | 기본 권장 모델 |
| Gemma 4 E2B | `gemma4:e2b` | 7.2GB | 128K | 8GB 메모리 장비용 |
| Gemma 4 26B A4B | `gemma4:26b` | 18GB | 256K | 32GB 이상, 성능 실험 |
| Gemma 4 31B | `gemma4:31b` | 20GB | 256K | 36GB 이상, 품질 우선 |

`B`는 Billion, 즉 10억 개 파라미터 규모를 뜻합니다. `26B`가 파일 크기 26GB라는 뜻은 아닙니다.

## 모델 선택

| 장비 | 기본 추천 | 추가 선택 | 비고 |
| --- | --- | --- | --- |
| Windows 8GB | `gemma4:e2b` | 없음 | 매우 느릴 수 있습니다. 가능하면 16GB 이상을 권장 |
| Windows 16GB | `gemma4:e4b` | 없음 | 기본 권장 |
| Windows 32GB 이상 | `gemma4:e4b` | `gemma4:26b` | GPU/VRAM도 함께 확인 |
| Apple Silicon Mac 8GB | `gemma4:e2b` | 없음 | 브라우저 탭과 무거운 앱을 줄이세요 |
| Apple Silicon Mac 16GB | `gemma4:e4b` | 없음 | 기본 권장 |
| Apple Silicon Mac 32GB 이상 | `gemma4:e4b` | `gemma4:26b` 또는 `gemma4:31b` | 큰 모델은 행사 전 반드시 테스트 |
| Intel Mac 8GB | `gemma4:e2b` | 없음 | Ollama 기준 CPU 전용이라 많이 느릴 수 있습니다 |
| Intel Mac 16GB 이상 | `gemma4:e4b` | 없음 | CPU 전용이라 응답이 늦을 수 있습니다 |

세부 기준은 [내 컴퓨터에 맞는 Gemma 4 모델 선택](../../docs/02-model-selection.md)에 있습니다.

## 운영체제별 준비 문서

| 환경 | 설치 문서 | 기본 추천 모델 |
| --- | --- | --- |
| Windows | [Windows 설치 가이드](../../docs/03-windows.md) | `gemma4:e4b` |
| macOS Apple Silicon | [macOS Apple Silicon 설치 가이드](../../docs/04-macos-apple-silicon.md) | `gemma4:e4b` |
| macOS Intel Mac | [macOS Intel Mac 설치 가이드](../../docs/05-macos-intel.md) | `gemma4:e4b` 또는 8GB 장비는 `gemma4:e2b` |

## 빠른 준비 명령

### Windows PowerShell

```powershell
uv --version
uv run python --version
Set-Location hands-on/session-1/work
uv sync
Set-Location ../../..
ollama --version
ollama pull gemma4:e4b
ollama run gemma4:e4b
Invoke-RestMethod http://localhost:11434/api/tags
```

8GB 메모리 장비일 경우:

```powershell
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

### macOS

```bash
uv --version
uv run python --version
cd hands-on/session-1/work
uv sync
cd ../../..
ollama --version
ollama pull gemma4:e4b
ollama run gemma4:e4b
curl http://localhost:11434/api/tags
```

8GB 메모리 장비일 경우:

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

## Ollama 서버와 API 테스트

Ollama 앱을 켜면 로컬 서버는 보통 자동으로 실행됩니다.

```text
http://localhost:11434
```

연결이 안 되면 Ollama 앱을 실행하거나 별도 터미널에서 다음 명령을 실행하세요.

```bash
ollama serve
```

행사 전에는 다음 중 하나 이상을 확인해 주세요.

- 모델 목록 확인: `GET /api/tags`
- Ollama Chat API 테스트: `POST /api/chat`
- OpenAI 호환 API 테스트: `POST /v1/chat/completions`

자세한 예시는 [Ollama 서버 및 API 테스트](../../docs/06-server-api-test.md)에 있습니다.

## 선택 준비: Google Antigravity 2.0, IDE, CLI

Google I/O 2026 발표 기준으로 Antigravity는 다음 세 가지 이름을 구분해서 이해하면 됩니다.

- Antigravity 2.0: IDE와 분리된 독립 데스크톱 앱입니다. Project 단위로 여러 폴더를 연결하고, 에이전트 실행과 결과물을 관리합니다.
- Antigravity IDE: 코드 편집기형 앱입니다. 실습 중 파일을 직접 열고 수정하거나 확장 프로그램을 써야 한다면 IDE 또는 기존 VS Code를 준비하세요.
- Antigravity CLI, AGY CLI: 터미널에서 `agy` 명령으로 실행하는 Antigravity 터미널 UI입니다. Antigravity 2.0과 같은 agent harness와 설정을 공유합니다.

Ollama와 Python 실습 자체에는 Antigravity가 필수는 아닙니다. 다만 행사에서 에이전트 기반 코드 생성 흐름을 따라 하려면 행사 전에 한 번 실행과 로그인까지 확인해 주세요. 회사/학교 계정이나 관리형 장비에서는 로그인, 설치, 실행 스크립트가 보안 정책으로 막힐 수 있습니다.

준비 기준:

- Antigravity 2.0 또는 IDE: https://antigravity.google/download 에서 운영체제에 맞는 설치 파일 다운로드
- Windows: 설치 프로그램 실행 후 앱 실행
- macOS Apple Silicon: DMG 설치 후 Applications 폴더에서 앱 실행
- macOS Intel Mac: 공식 Antigravity 2.0 데스크톱 앱은 x86 미지원으로 표시되므로 Antigravity IDE 또는 기존 VS Code 같은 편집기를 준비
- 첫 실행 설정 완료
- 사용 가능한 Google 계정으로 로그인 가능 여부 확인
- 행사 자료 폴더를 열 수 있는지 확인
- Antigravity 2.0을 쓸 경우 Project에 이 저장소 루트 폴더 추가
- 이 저장소의 `.agents/rules`, `.agents/workflows`, `.agents/skills` 설정 확인

Antigravity CLI를 사용할 경우:

가능하면 Antigravity 2.0 또는 Antigravity IDE에서 먼저 로그인해 둡니다. 저장된 세션이 없으면 `agy` 첫 실행 중 브라우저 기반 Google 로그인이 열릴 수 있습니다.

이미 설치되어 있다면 버전 확인부터 진행합니다.

```bash
agy --version
agy
```

설치가 필요하면 Mac/Linux에서는 다음 명령을 사용합니다.

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
agy --version
```

Windows PowerShell에서는 다음 설치 명령을 사용합니다.

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
agy --version
agy
```

행사 자료 저장소 루트에서 `agy`를 실행한 뒤, CLI 입력창에서 다음 기본 명령을 확인해 보세요.

```text
?
/usage
/permissions
/skills
/mcp
/tasks
```

간단한 읽기 전용 테스트 프롬프트:

```text
현재 폴더의 파일 구성을 읽고 Session 1 사전 준비에서 확인해야 할 항목만 요약해 줘. 파일은 수정하지 마.
```

이 저장소에는 행사 실습용 Antigravity 설정이 들어 있습니다.

- Rules: `.agents/rules/`에 공통 코딩 규칙을 둡니다.
- Workflows: `.agents/workflows/`에 반복 실습 절차를 두고 Agent 입력창에서 `/workflow-name`으로 실행합니다.
- Skills: `.agents/skills/<skill-name>/SKILL.md`에 특정 작업용 지식과 절차를 둘 수 있습니다.

자세한 설치와 설정 흐름은 [Google Antigravity 2.0 및 CLI 준비 가이드](../../docs/07-google-antigravity.md)에 있습니다.

## 행사 전 최종 체크리스트

Windows:

- `uv --version` 성공
- `uv run python --version` 성공
- PowerShell에서 `ollama --version` 성공
- `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e4b`로 1회 답변 생성 성공
- 8GB 메모리 장비는 `gemma4:e2b`로 준비
- `Invoke-RestMethod http://localhost:11434/api/tags` 성공

Apple Silicon Mac:

- `uname -m` 결과가 `arm64`
- `uv --version` 성공
- `uv run python --version` 성공
- `ollama --version` 성공
- `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e4b`로 1회 답변 생성 성공
- 8GB 메모리 장비는 `gemma4:e2b`로 준비
- `curl http://localhost:11434/api/tags` 성공

Intel Mac:

- `uname -m` 결과가 `x86_64`
- macOS 14 이상 확인
- `uv --version` 성공
- `uv run python --version` 성공
- `ollama --version` 성공
- 16GB 이상이면 `ollama pull gemma4:e4b` 완료
- 16GB 이상이면 `ollama run gemma4:e4b`로 1회 답변 생성 성공
- 8GB 메모리 장비는 `gemma4:e2b`로 준비
- `curl http://localhost:11434/api/tags` 성공

Google Antigravity를 사용할 경우:

- Antigravity 2.0 또는 IDE를 사용할 경우 앱 실행 성공
- 사용 가능한 Google 계정 로그인 성공
- Antigravity 2.0을 사용할 경우 Project에 행사 자료 폴더 추가
- Antigravity IDE 또는 기존 편집기를 사용할 경우 행사 자료 폴더 열기 성공
- Antigravity CLI를 사용할 경우 `agy --version` 성공
- Antigravity CLI에서 `?`, `/usage`, `/permissions`, `/skills`, `/mcp`, `/tasks` 입력 성공
- `.agents/rules`, `.agents/workflows`, `.agents/skills` 확인
- Python 핸즈온을 진행할 경우 `hands-on/session-1/work`에서 `uv sync` 성공
- Python 핸즈온을 진행할 경우 `/session-1-01-ollama-server-api`, `/session-1-02-adk-ollama` workflow 확인

문제가 생기면 [최종 체크리스트와 문제 해결](../../docs/10-checklist-troubleshooting.md)를 참고하세요.

## 문서 목록

1. [Ollama와 Gemma 4 개요](../../docs/01-ollama-gemma4-overview.md)
2. [내 컴퓨터에 맞는 Gemma 4 모델 선택](../../docs/02-model-selection.md)
3. [Windows 설치 가이드](../../docs/03-windows.md)
4. [macOS Apple Silicon 설치 가이드](../../docs/04-macos-apple-silicon.md)
5. [macOS Intel Mac 설치 가이드](../../docs/05-macos-intel.md)
6. [Ollama 서버 및 API 테스트](../../docs/06-server-api-test.md)
7. [Google Antigravity 2.0 및 CLI 준비 가이드](../../docs/07-google-antigravity.md)
8. [Gemma 4 Python 핸즈온 생성 프롬프트](../../docs/08-python-hands-on.md)
9. [Python + uv 설치 가이드](../../docs/09-python-uv-setup.md)
10. [최종 체크리스트와 문제 해결](../../docs/10-checklist-troubleshooting.md)
11. [공식 참고 링크](../../docs/11-references.md)

## 공식 참고 링크

- Ollama 다운로드: https://ollama.com/download
- Ollama macOS 문서: https://docs.ollama.com/macos
- Ollama Gemma 4 모델 페이지: https://ollama.com/library/gemma4
- Ollama API 문서: https://docs.ollama.com/api/introduction
- Ollama OpenAI 호환 API 문서: https://docs.ollama.com/api/openai-compatibility
- uv 설치 문서: https://docs.astral.sh/uv/getting-started/installation/
- uv Python 설치 문서: https://docs.astral.sh/uv/guides/install-python/
- Google Gemma 4 출시 글: https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
- Google Antigravity 다운로드: https://antigravity.google/download
- Introducing Google Antigravity 2.0: https://antigravity.google/blog/introducing-google-antigravity-2-0
- Google Antigravity CLI: https://antigravity.google/blog/introducing-google-antigravity-cli
- Gemini CLI에서 Antigravity CLI로 전환 안내: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- Google Antigravity Rules / Workflows: https://antigravity.google/docs/rules-workflows
- Google Antigravity Skills: https://antigravity.google/docs/skills
