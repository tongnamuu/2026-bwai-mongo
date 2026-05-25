# macOS Intel Mac 설치 가이드

[메인 안내로 돌아가기](../README.md)

## 대상

- macOS 14 Sonoma 이상
- Intel Mac
- Ollama 기준 CPU 전용

Ollama 공식 macOS 문서는 Apple M series는 CPU/GPU 지원, x86 Mac은 CPU 전용으로 안내합니다. 즉 Intel Mac에 GPU가 없다는 뜻은 아니지만, Ollama에서는 GPU 가속을 기대하지 않는 편이 맞습니다.

Intel Mac은 Apple Silicon Mac보다 로컬 LLM 실행이 훨씬 느릴 수 있습니다. 16GB 이상 장비는 행사 기본 모델인 `gemma4:e4b`를 먼저 준비하고, 8GB 장비만 `gemma4:e2b`를 준비하세요.

## 1. 내 Mac 확인

터미널에서 실행합니다.

```bash
uname -m
sw_vers -productVersion
```

결과가 `x86_64`이면 Intel Mac입니다.

macOS 버전이 14 미만이고 업데이트할 수 없다면 Ollama 최신 설치 요구사항에 못 미칠 수 있습니다. 가능하면 다른 노트북을 준비하세요.

## 2. Python + uv 준비

Python 핸즈온 실습을 진행할 경우 먼저 [Python + uv 설치 가이드](./09-python-uv-setup.md)를 완료하세요.

완료 기준:

- 터미널에서 `uv --version` 성공
- 터미널에서 `uv run python --version` 성공

## 3. Ollama 설치

1. https://ollama.com/download/mac으로 이동합니다.
2. macOS용 `ollama.dmg`를 다운로드합니다.
3. DMG를 열고 Ollama 앱을 `Applications` 폴더로 옮깁니다.
4. Ollama 앱을 한 번 실행합니다.
5. CLI 경로 연결을 요청하면 허용합니다.

## 4. 설치 확인

```bash
ollama --version
```

## 5. Gemma 4 모델 다운로드

```bash
ollama pull gemma4:e4b
```

8GB 메모리 장비:

```bash
ollama pull gemma4:e2b
```

## 6. 실행 테스트

```bash
ollama run gemma4:e4b
```

프롬프트가 열리면 다음 문장을 입력합니다.

```text
Bwai Mongo 행사 준비 테스트입니다. 한 문장으로 응답해 주세요.
```

Intel Mac에서 응답이 늦게 나오는 것은 정상일 수 있습니다. 테스트할 때 브라우저 탭, 영상 회의 앱, 무거운 개발 도구를 최대한 닫고 전원 어댑터를 연결하세요.

## 7. 다음 단계

설치와 실행 테스트가 끝나면 [Ollama 서버 및 API 테스트](./06-server-api-test.md)로 넘어가세요.
