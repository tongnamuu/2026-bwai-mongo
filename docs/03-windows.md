# Windows 설치 가이드

[메인 안내로 돌아가기](../README.md)

## 대상

- Windows 10 22H2 이상
- PowerShell 사용 권장
- NVIDIA 또는 AMD GPU가 있으면 최신 드라이버 설치 권장

## 1. Python + uv 준비

Python 핸즈온 실습을 진행할 경우 먼저 [Python + uv 설치 가이드](./09-python-uv-setup.md)를 완료하세요.

완료 기준:

- PowerShell에서 `uv --version` 성공
- PowerShell에서 `uv run python --version` 성공

## 2. Ollama 설치

방법 A: 공식 설치 프로그램

1. https://ollama.com/download/windows로 이동합니다.
2. `OllamaSetup.exe`를 다운로드합니다.
3. 설치 프로그램을 실행합니다.
4. 설치 후 PowerShell을 새로 엽니다.

방법 B: PowerShell 설치 명령

```powershell
irm https://ollama.com/install.ps1 | iex
```

회사/학교 장비에서는 보안 정책 때문에 스크립트 실행이 막힐 수 있습니다. 이 경우 방법 A의 설치 프로그램을 사용하세요.

## 3. 설치 확인

PowerShell에서 실행합니다.

```powershell
ollama --version
```

버전이 출력되면 설치된 상태입니다. 명령을 찾을 수 없다는 메시지가 나오면 PowerShell 창을 닫고 새로 열어 다시 실행하세요.

## 4. Gemma 4 모델 다운로드

기본 준비:

```powershell
ollama pull gemma4:e4b
```

8GB 메모리 장비:

```powershell
ollama pull gemma4:e2b
```

32GB 이상에서 큰 모델을 실험할 경우:

```powershell
ollama pull gemma4:26b
```

## 5. 실행 테스트

```powershell
ollama run gemma4:e4b
```

프롬프트가 열리면 다음 문장을 입력합니다.

```text
Bwai Mongo 행사 준비 테스트입니다. Ollama가 무엇인지 한 문장으로 설명해 주세요.
```

종료하려면 `/bye`를 입력하거나 `Ctrl + D`를 누릅니다.

## 6. 다음 단계

설치와 실행 테스트가 끝나면 [Ollama 서버 및 API 테스트](./06-server-api-test.md)로 넘어가세요.
