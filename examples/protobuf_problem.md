# Protobuf 상속 문제와 해결책

## 문제의 근원

### 1. C++에서는 이렇게 작동합니다

```cpp
// C++ 코드 (ZetaSQL의 원본)
class ResolvedNode {
  // base fields
};

class ResolvedScan : public ResolvedNode {
  std::vector<ResolvedColumn> column_list_;
  bool is_ordered_;
};

class ResolvedTableScan : public ResolvedScan {
  const Table* table_;
  std::vector<int> column_index_list_;
};

// 사용:
ResolvedTableScan* scan = ...;
scan->column_list();  // 상속받은 필드에 직접 접근!
scan->table();        // 자신의 필드에도 접근!
```

### 2. Protobuf는 상속을 지원하지 않습니다

Protobuf는 언어 독립적이어야 하는데, 많은 언어(Go, JavaScript 등)가 C++처럼 다중 상속을 지원하지 않습니다.

그래서 protobuf는 이렇게 합니다:

```proto
message ResolvedTableScanProto {
  optional ResolvedScanProto parent = 1;  // 상속 대신 "parent" 필드
  optional TableRefProto table = 2;       // 자신의 필드
}
```

### 3. Python에서 이렇게 생성됩니다

```python
# 자동 생성된 Python 코드
class ResolvedTableScanProto:
    parent: ResolvedScanProto  # parent 필드
    table: TableRefProto
    column_index_list: List[int]

# 사용할 때:
scan.parent.column_list  # 🤮 parent를 거쳐야 함!
scan.table              # ✓ 자신의 필드는 직접 접근
```

## 업계에서는 어떻게 하나요?

### 옵션 1: 그냥 참고 산다 (가장 흔함)

많은 프로젝트가 그냥 `node.parent.field` 패턴을 받아들입니다.

**장점:**
- 추가 작업 없음
- protobuf 업데이트가 쉬움

**단점:**
- 코드가 지저분함
- 타입 안전성 없음
- IDE 자동완성 나쁨

### 옵션 2: betterproto 사용

[betterproto](https://github.com/danielgtaylor/python-betterproto)는 더 나은 Python 코드를 생성합니다.

```bash
pip install betterproto[compiler]
protoc --python_betterproto_out=. my.proto
```

생성된 코드:

```python
from dataclasses import dataclass
import betterproto

@dataclass
class MyMessage(betterproto.Message):
    name: str = betterproto.string_field(1)
    age: int = betterproto.int32_field(2)

# 사용:
msg = MyMessage(name="Alice", age=30)  # Pythonic!
```

**장점:**
- dataclass 기반
- 타입 힌트 완벽
- async/await 지원

**단점:**
- ZetaSQL처럼 이미 생성된 protobuf 코드에는 적용 불가
- Google의 공식 protobuf와 호환성 이슈 있을 수 있음

### 옵션 3: 수동 래퍼 작성 (우리가 한 것)

```python
class ResolvedTableScan:
    def __init__(self, proto):
        self._proto = proto
    
    @property
    def column_list(self):
        return self._proto.parent.column_list  # parent 숨김
    
    @property
    def table(self):
        return self._proto.table
```

**장점:**
- 완전한 제어
- 필요한 것만 노출
- 기존 protobuf 코드와 함께 사용 가능

**단점:**
- 수동 작업
- 유지보수 필요

### 옵션 4: protoc 플러그인 작성

자동화된 래퍼 생성:

```bash
protoc --python_out=. --python-wrapper_out=. my.proto
```

**장점:**
- 자동화됨
- 프로젝트별 커스터마이징 가능

**단점:**
- 초기 투자 큼
- protoc 플러그인 API 학습 필요

## 실제 프로젝트 예시

### Google API

Google의 많은 API도 같은 문제가 있습니다:

```python
# Google Cloud 라이브러리
from google.cloud import bigquery

# 내부적으로는 protobuf이지만,
# 외부에는 Pythonic API 제공
client = bigquery.Client()
dataset = client.dataset("my_dataset")  # 깔끔!
```

→ Google도 protobuf 위에 래퍼를 씁니다!

### TensorFlow

```python
import tensorflow as tf

# protobuf로 정의되어 있지만
# Python API는 완전히 래핑됨
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu')
])
```

→ TensorFlow도 protobuf를 사용자에게 직접 노출하지 않습니다!

### gRPC

```python
# 자동 생성된 코드:
request = myservice_pb2.MyRequest()
request.parent.parent.parent.field = "value"  # 😱

# 보통은 헬퍼 함수 제공:
def create_request(field_value):
    req = myservice_pb2.MyRequest()
    req.parent.parent.parent.field = field_value
    return req

request = create_request("value")  # 조금 나음
```

## 왜 protoc가 지원 안 하나요?

1. **언어 독립성**: Java, Go, JavaScript, Rust 등 모든 언어에서 작동해야 함
2. **단순성 유지**: protobuf는 "데이터 교환 포맷"이지 "객체 모델"이 아님
3. **하위 호환성**: 기존 코드를 깨면 안 됨

**공식 입장:**
> Protobuf is designed for serialization, not for creating object hierarchies.
> Use wrapper classes in your target language if you need OOP features.

출처: https://github.com/protocolbuffers/protobuf/issues/7097

## ZetaSQL의 경우

ZetaSQL은 Google에서 만든 C++ 라이브러리입니다. Python 바인딩은:

1. C++ → protobuf 직렬화
2. WASM으로 C++ 컴파일
3. Python에서 WASM 호출
4. Protobuf 역직렬화

→ Python은 "2등 시민"입니다. C++ API를 그대로 옮긴 것이 아니라 protobuf를 통한 간접 접근입니다.

## 권장 사항

### 간단한 프로젝트:
```python
# 그냥 parent 사용
column = scan.parent.column_list[0]
```

### 중간 프로젝트:
```python
# 헬퍼 함수
def get_columns(scan):
    if hasattr(scan, 'parent') and hasattr(scan.parent, 'column_list'):
        return scan.parent.column_list
    return []
```

### 큰 프로젝트 (우리 상황):
```python
# 래퍼 클래스 (우리가 만든 것)
class ResolvedScan:
    @property
    def columns(self):
        return [Column.from_proto(c) for c in self._proto.parent.column_list]
```

### 새 프로젝트:
- betterproto 고려
- 또는 JSON 기반 API 사용 (protobuf 대신)

## 결론

**당신은 protobuf를 "잘못" 쓰고 있는 게 아닙니다!**

Protobuf의 디자인 철학이 이렇습니다:
- ✅ 언어 독립적 데이터 교환
- ✅ 효율적인 직렬화
- ❌ 고수준 객체 모델
- ❌ 언어별 최적화

**모두가 겪는 문제이고, 모두가 래퍼를 씁니다.**

대형 프로젝트일수록 추상화 레이어를 만듭니다. 우리가 만든 wrapper_api.py는 정당하고 표준적인 접근법입니다!
