# Session 1 사전 준비 가이드

Ollama와 Gemma 4 모델, Python, `uv`를 행사 전에 준비합니다.

행사 당일에 처음 Ollama, `uv`, Python 패키지, Gemma 4 모델을 다운로드하는 방식은 피하는 것이 좋습니다. Gemma 4 모델은 작은 모델도 수 GB라서, 현장 네트워크 상태에 따라 다운로드에 시간이 오래 걸릴 수 있습니다. 행사 전까지 다음 항목을 마쳐 주세요.

1. Ollama 설치 완료
2. Gemma 4 모델 다운로드 완료
3. 터미널 실행 테스트와 API 테스트 1회 성공
4. Python + `uv` 설치와 패키지 설치 테스트 성공
5. 코드 편집기를 사용할 경우 Google Antigravity 또는 기존 편집기 실행 확인
6. Antigravity를 사용할 경우 workspace rules, workflows, skills 설정 위치 확인

## 대상

이 문서는 Ollama로 로컬 LLM 서버와 API를 준비하는 다음 환경을 대상으로 합니다.

- Windows 노트북
- macOS Apple Silicon Mac
- macOS Intel Mac

Linux, ChromeOS, LM Studio, llama.cpp 같은 다른 경로는 이 문서의 범위에서 제외합니다.
코드 편집기는 Google Antigravity를 선택 준비 항목으로 다룹니다.

## 준비 요약

- 16GB 이상 Windows 또는 Apple Silicon Mac이면 `gemma4:e4b`까지 준비하면 좋습니다.
- 8GB 메모리 장비는 운영체제와 관계없이 `gemma4:e2b`만 준비하는 것을 권장합니다.
- Intel Mac은 Ollama 공식 macOS 지원 기준에서 CPU 전용입니다. Mac에 GPU가 없다는 뜻은 아니지만, Ollama에서는 GPU 가속을 기대하지 말고 `gemma4:e2b`를 기본으로 준비하세요.
- `gemma4:latest`는 나중에 바뀔 수 있으므로 행사 준비에서는 명시적 태그를 쓰세요.
- Ollama 서버 기본 주소는 `http://localhost:11434`입니다.
- Python 핸즈온을 진행하려면 [Python + uv 설치 가이드](../../docs/09-python-uv-setup.md)를 먼저 확인하세요.
- 코드 편집기가 필요하면 [Google Antigravity 설치 가이드](../../docs/07-google-antigravity.md)를 확인하세요.
- 60분 실습용 Python 생성 프롬프트는 [Gemma 4 Python 핸즈온 생성 프롬프트](../../docs/08-python-hands-on.md)를 확인하세요.

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
| Gemma 4 E2B | `gemma4:e2b` | 7.2GB | 128K | 8GB 또는 Intel Mac 기본 |
| Gemma 4 E4B | `gemma4:e4b` | 9.6GB | 128K | 16GB 이상 기본 |
| Gemma 4 26B A4B | `gemma4:26b` | 18GB | 256K | 32GB 이상, 성능 실험 |
| Gemma 4 31B | `gemma4:31b` | 20GB | 256K | 36GB 이상, 품질 우선 |

`B`는 Billion, 즉 10억 개 파라미터 규모를 뜻합니다. `26B`가 파일 크기 26GB라는 뜻은 아닙니다.

## 모델 선택

| 장비 | 기본 추천 | 추가 선택 | 비고 |
| --- | --- | --- | --- |
| Windows 8GB | `gemma4:e2b` | 없음 | 매우 느릴 수 있습니다. 가능하면 16GB 이상을 권장 |
| Windows 16GB | `gemma4:e4b` | `gemma4:e2b` | 실패 시 E2B로 낮추세요 |
| Windows 32GB 이상 | `gemma4:e4b` | `gemma4:26b` | GPU/VRAM도 함께 확인 |
| Apple Silicon Mac 8GB | `gemma4:e2b` | 없음 | 브라우저 탭과 무거운 앱을 줄이세요 |
| Apple Silicon Mac 16GB | `gemma4:e4b` | `gemma4:e2b` | 대부분 이 조합이면 충분 |
| Apple Silicon Mac 32GB 이상 | `gemma4:e4b` | `gemma4:26b` 또는 `gemma4:31b` | 큰 모델은 행사 전 반드시 테스트 |
| Intel Mac | `gemma4:e2b` | `gemma4:e4b` | Ollama 기준 CPU 전용이라 많이 느릴 수 있습니다 |

세부 기준은 [내 컴퓨터에 맞는 Gemma 4 모델 선택](../../docs/02-model-selection.md)에 있습니다.

## 운영체제별 준비 문서

| 환경 | 설치 문서 | 기본 추천 모델 |
| --- | --- | --- |
| Windows | [Windows 설치 가이드](../../docs/03-windows.md) | `gemma4:e2b` 또는 `gemma4:e4b` |
| macOS Apple Silicon | [macOS Apple Silicon 설치 가이드](../../docs/04-macos-apple-silicon.md) | `gemma4:e2b` 또는 `gemma4:e4b` |
| macOS Intel Mac | [macOS Intel Mac 설치 가이드](../../docs/05-macos-intel.md) | `gemma4:e2b` |

## 빠른 준비 명령

### Windows PowerShell

```powershell
uv --version
uv run python --version
ollama --version
ollama pull gemma4:e2b
ollama run gemma4:e2b
Invoke-RestMethod http://localhost:11434/api/tags
```

16GB 이상 장비에서 E4B까지 준비할 경우:

```powershell
ollama pull gemma4:e4b
ollama run gemma4:e4b
```

### macOS

```bash
uv --version
uv run python --version
ollama --version
ollama pull gemma4:e2b
ollama run gemma4:e2b
curl http://localhost:11434/api/tags
```

16GB 이상 장비에서 E4B까지 준비할 경우:

```bash
ollama pull gemma4:e4b
ollama run gemma4:e4b
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

## 코드 편집기: Google Antigravity

Google Antigravity는 Google의 agent-first 개발 환경입니다. 이번 행사에서 코드를 열어보고 수정해야 한다면 기존 VS Code를 사용해도 되고, Antigravity를 미리 설치해도 됩니다.

Antigravity는 현재 preview 성격의 도구이며, Google Codelab 기준으로 개인 Gmail 계정으로 시작하는 흐름을 안내합니다. 회사/학교 계정이나 관리형 장비에서는 로그인 또는 설치 정책 때문에 막힐 수 있으므로 행사 전에 한 번 실행까지 확인해 주세요.

준비 기준:

- https://antigravity.google/download 에서 운영체제에 맞는 설치 파일 다운로드
- Windows: 설치 프로그램 실행 후 앱 실행
- macOS: DMG 설치 후 Applications 폴더에서 앱 실행
- 첫 실행 설정 완료
- 개인 Gmail 계정으로 로그인 가능 여부 확인
- 행사 자료 폴더를 열 수 있는지 확인
- 이 저장소의 `.agents/rules`, `.agents/workflows`, `.agents/skills` 설정 확인

이 저장소에는 행사 실습용 Antigravity workspace 설정이 들어 있습니다.

- Rules: `.agents/rules/`에 공통 코딩 규칙을 둡니다.
- Workflows: `.agents/workflows/`에 반복 실습 절차를 두고 Agent 입력창에서 `/workflow-name`으로 실행합니다.
- Skills: `.agents/skills/<skill-name>/SKILL.md`에 특정 작업용 지식과 절차를 둘 수 있습니다.

자세한 설치와 설정 흐름은 [Google Antigravity 설치 가이드](../../docs/07-google-antigravity.md)에 있습니다.

## 행사 전 최종 체크리스트

Windows:

- `uv --version` 성공
- `uv run python --version` 성공
- PowerShell에서 `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `Invoke-RestMethod http://localhost:11434/api/tags` 성공

Apple Silicon Mac:

- `uname -m` 결과가 `arm64`
- `uv --version` 성공
- `uv run python --version` 성공
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공

Intel Mac:

- `uname -m` 결과가 `x86_64`
- macOS 14 이상 확인
- `uv --version` 성공
- `uv run python --version` 성공
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공

Google Antigravity를 사용할 경우:

- Antigravity 앱 실행 성공
- 개인 Gmail 계정 로그인 성공
- 행사 자료 폴더 열기 성공
- `.agents/rules`, `.agents/workflows`, `.agents/skills` 확인
- Python 핸즈온을 진행할 경우 `/session-1-01-gemini-api`, `/session-1-02-adk-gemini-api`, `/session-1-03-ollama-server-api`, `/session-1-04-adk-ollama` workflow 확인

문제가 생기면 [최종 체크리스트와 문제 해결](../../docs/10-checklist-troubleshooting.md)를 참고하세요.

## 문서 목록

1. [Ollama와 Gemma 4 개요](../../docs/01-ollama-gemma4-overview.md)
2. [내 컴퓨터에 맞는 Gemma 4 모델 선택](../../docs/02-model-selection.md)
3. [Windows 설치 가이드](../../docs/03-windows.md)
4. [macOS Apple Silicon 설치 가이드](../../docs/04-macos-apple-silicon.md)
5. [macOS Intel Mac 설치 가이드](../../docs/05-macos-intel.md)
6. [Ollama 서버 및 API 테스트](../../docs/06-server-api-test.md)
7. [Google Antigravity 설치 가이드](../../docs/07-google-antigravity.md)
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
- Gemini API Quickstart: https://ai.google.dev/gemini-api/docs/quickstart
- Gemini API 키 안내: https://ai.google.dev/gemini-api/docs/api-key
- Google Gemma 4 출시 글: https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
- Google Antigravity 다운로드: https://antigravity.google/download
- Google Antigravity Codelab: https://codelabs.developers.google.com/getting-started-google-antigravity
- Google Antigravity Rules / Workflows: https://antigravity.google/docs/rules-workflows
- Google Antigravity Skills: https://antigravity.google/docs/skills
