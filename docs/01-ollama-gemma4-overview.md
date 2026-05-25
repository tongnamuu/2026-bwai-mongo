# Ollama와 Gemma 4 개요

[메인 안내로 돌아가기](../README.md)

## Ollama 개요

Ollama는 로컬 컴퓨터에서 LLM을 다운로드하고 실행하는 도구입니다. 설치하면 터미널에서 `ollama run`, `ollama pull` 같은 명령을 사용할 수 있고, 로컬 API 서버는 기본적으로 `http://localhost:11434`에서 동작합니다.

이번 행사에서는 Ollama를 다음 용도로 사용합니다.

- Gemma 4 모델을 내 노트북에 미리 다운로드
- 인터넷 없이도 로컬에서 모델 실행
- 터미널에서 간단한 대화 테스트
- 로컬 API 서버를 통해 앱, 스크립트, 에이전트 도구와 연결

Ollama는 모델 파일과 설정을 홈 디렉터리 아래에 저장합니다. 모델 파일이 커질 수 있으니 최소 20GB, 가능하면 40GB 이상 여유 공간을 확보해 주세요.

## Gemma 4 개요

Gemma 4는 Google DeepMind가 공개한 오픈 모델 계열입니다. Google 공식 블로그는 Gemma 4가 고급 추론, 에이전트형 워크플로우, 코드 생성, 멀티모달 입력, 긴 컨텍스트를 목표로 설계됐다고 설명합니다.

이번 행사에서는 Ollama에서 바로 실행 가능한 다음 태그를 기준으로 준비합니다.

| 모델 | Ollama 태그 | 표시 크기 | 컨텍스트 | 권장 환경 |
| --- | --- | ---: | ---: | --- |
| Gemma 4 E4B | `gemma4:e4b` | 9.6GB | 128K | 기본 권장 모델 |
| Gemma 4 E2B | `gemma4:e2b` | 7.2GB | 128K | 8GB 메모리 장비용 |
| Gemma 4 26B A4B | `gemma4:26b` | 18GB | 256K | 32GB 이상, 성능 실험 |
| Gemma 4 31B | `gemma4:31b` | 20GB | 256K | 36GB 이상, 품질 우선 |

## 꼭 알아둘 점

- `B`는 Billion, 즉 10억 개 파라미터 규모를 뜻합니다. `26B`가 파일 크기 26GB라는 뜻은 아닙니다.
- `26B A4B`는 전체 모델은 약 26B 규모이지만, 답변 생성 시 약 4B 규모가 활성화되는 MoE 계열 모델입니다.
- MoE 모델도 전체 모델 파일은 메모리에 올라가야 하므로 4B 모델처럼 가볍지는 않습니다.
- `gemma4:latest`는 현재 E4B 계열로 표시되지만 나중에 바뀔 수 있습니다.
- 사전 준비에는 `gemma4:e4b`, `gemma4:e2b`, `gemma4:26b`, `gemma4:31b`처럼 명시적 태그를 사용하세요.
- 이 문서의 기본 준비 모델은 `gemma4:e4b`입니다. 8GB 메모리 장비에서만 `gemma4:e2b`를 대체 모델로 준비하세요.

## 다음에 볼 문서

- 모델 선택이 필요하면 [내 컴퓨터에 맞는 Gemma 4 모델 선택](./02-model-selection.md)
- 설치를 시작하려면 [Windows 설치 가이드](./03-windows.md), [macOS Apple Silicon 설치 가이드](./04-macos-apple-silicon.md), [macOS Intel Mac 설치 가이드](./05-macos-intel.md)
- 설치 후에는 [Ollama 서버 및 API 테스트](./06-server-api-test.md)
