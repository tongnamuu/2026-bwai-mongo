# macOS Apple Silicon 설치 가이드

[메인 안내로 돌아가기](../README.md)

## 대상

- macOS 14 Sonoma 이상
- macOS Apple Silicon Mac
- 터미널 사용

## 1. 내 Mac 확인

터미널에서 실행합니다.

```bash
uname -m
sw_vers -productVersion
```

결과가 `arm64`이면 Apple Silicon Mac입니다.

## 2. Python + uv 준비

Python 핸즈온 실습을 진행할 경우 먼저 [Python + uv 설치 가이드](./09-python-uv-setup.md)를 완료하세요.

완료 기준:

- 터미널에서 `uv --version` 성공
- 터미널에서 `uv run python --version` 성공

## 3. Ollama 설치

방법 A: 공식 앱 설치

1. https://ollama.com/download/mac으로 이동합니다.
2. macOS용 `ollama.dmg`를 다운로드합니다.
3. DMG를 열고 Ollama 앱을 `Applications` 폴더로 옮깁니다.
4. Ollama 앱을 한 번 실행합니다.
5. CLI 경로 연결을 요청하면 허용합니다.

방법 B: 터미널 설치 명령

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

일반적인 준비에는 방법 A가 더 편합니다.

## 4. 설치 확인

터미널을 새로 열고 실행합니다.

```bash
ollama --version
```

## 5. Gemma 4 모델 다운로드

기본 준비:

```bash
ollama pull gemma4:e4b
```

8GB 메모리 장비:

```bash
ollama pull gemma4:e2b
```

32GB 이상에서 큰 모델을 실험할 경우:

```bash
ollama pull gemma4:26b
```

## 6. 실행 테스트

```bash
ollama run gemma4:e4b
```

프롬프트가 열리면 다음 문장을 입력합니다.

```text
Bwai Mongo 행사 준비 테스트입니다. Gemma 4의 장점을 세 가지로 요약해 주세요.
```

종료하려면 `/bye`를 입력하거나 `Ctrl + D`를 누릅니다.

## 7. 다음 단계

설치와 실행 테스트가 끝나면 [Ollama 서버 및 API 테스트](./06-server-api-test.md)로 넘어가세요.
