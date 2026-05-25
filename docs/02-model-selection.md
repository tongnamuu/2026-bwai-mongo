# 내 컴퓨터에 맞는 Gemma 4 모델 선택

[메인 안내로 돌아가기](../README.md)

## 준비 요약

이번 행사 기본 모델은 `gemma4:e4b`입니다. 8GB 메모리 장비만 `gemma4:e2b`를 대체 모델로 준비하세요. 행사장에서 처음 다운로드하지 않도록 본인 장비에 맞는 모델을 미리 받아 두는 것이 중요합니다.

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

## 모델별 준비 기준

### `gemma4:e2b`

8GB 메모리 장비용 대체 모델입니다.

- 8GB 장비
- 큰 모델 다운로드가 부담되는 경우

### `gemma4:e4b`

이번 행사 기본 권장 모델입니다.

- Windows 16GB 이상
- Apple Silicon Mac 16GB 이상
- Intel Mac 16GB 이상
- E2B보다 조금 더 나은 답변 품질을 기대하는 경우

### `gemma4:26b`

32GB 이상 장비에서 실험할 수 있는 큰 모델입니다.

- 충분한 메모리와 디스크 여유가 있는 경우
- 큰 모델을 행사 전에 이미 테스트할 수 있는 경우
- 성능과 품질을 더 확인하고 싶은 경우

### `gemma4:31b`

36GB 이상 장비에서 품질 우선으로 시도할 수 있는 모델입니다.

- 일반적인 기본 준비용으로는 권장하지 않습니다.
- 다운로드와 실행 테스트를 행사 전에 반드시 끝내야 합니다.

## 모델 선택 시 주의

- 행사 당일에 큰 모델을 처음 다운로드하지 마세요.
- 8GB 장비는 작은 모델에서도 속도가 많이 느릴 수 있습니다.
- Intel Mac은 Ollama 공식 macOS 지원 기준에서 CPU 전용입니다. Mac에 GPU가 없다는 뜻은 아니지만, Ollama에서는 GPU 가속을 기대하지 않는 편이 맞습니다.
- Windows에서 전용 GPU가 있어도 VRAM이 부족하면 큰 모델 실행이 느리거나 실패할 수 있습니다.
- `gemma4:latest` 대신 명시적인 태그를 사용하세요.

## 다음에 볼 문서

- [Windows 설치 가이드](./03-windows.md)
- [macOS Apple Silicon 설치 가이드](./04-macos-apple-silicon.md)
- [macOS Intel Mac 설치 가이드](./05-macos-intel.md)
