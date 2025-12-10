# Memgraph Cypher 파일

## 파일 정보

- **파일명**: `memgraph.cypher`
- **생성 스크립트**: `generate_memgraph_cypher.py`
- **기준 파일**: `context.txt`

## 구조

### 노드 타입

1. **Classification (분류)**
   - `id`: 분류 ID (예: C01010001)
   - `name`: 분류명
   - `display_name`: 표시명 (형식: "분류명 (Classification)")
   - `group`: 그룹 여부 (boolean)
   - `level`: 계층 레벨 (0: 도메인, 1: 중분류, 2: 소분류)

2. **Term (용어)**
   - `id`: 용어 ID (예: T01010001)
   - `name_ko`: 한글 용어명
   - `name_en`: 영문 용어명
   - `acronym`: 약어 (선택)
   - `display_name`: 표시명 (형식: "한글명 (Term)")

### 관계

1. **PARENT_OF**: 분류 계층 관계
   - (상위 분류)-[:PARENT_OF]->(하위 분류)
   - 예: (C01000001)-[:PARENT_OF]->(C01010001)

2. **BELONGS_TO**: 용어-분류 연결
   - (용어)-[:BELONGS_TO]->(분류)
   - 예: (T01010001)-[:BELONGS_TO]->(C01010001)

## 통계

- 분류(Classification) 노드: 90개
- 용어(Term) 노드: 148개
- PARENT_OF 관계: 83개
- BELONGS_TO 관계: 148개

## 사용법

### Memgraph Lab에서 실행

1. Memgraph Lab 실행
2. Query 탭에서 파일 내용 복사/붙여넣기
3. 실행

### mgconsole에서 실행

```bash
mgconsole < memgraph.cypher
```

### Python에서 실행

```python
from gqlalchemy import Memgraph

memgraph = Memgraph()

# 파일 읽기
with open('memgraph.cypher', 'r') as f:
    queries = f.read().split(';')

# 각 쿼리 실행
for query in queries:
    if query.strip():
        memgraph.execute(query)
```

## 재생성

context.txt를 수정한 후 재생성:

```bash
python3 generate_memgraph_cypher.py
```

## 쿼리 예시

### 특정 도메인의 모든 분류 조회

```cypher
MATCH (parent:Classification {id: 'C01000001'})-[:PARENT_OF*0..]->(child:Classification)
RETURN parent, child;
```

### 특정 분류의 모든 용어 조회

```cypher
MATCH (term:Term)-[:BELONGS_TO]->(clsf:Classification {id: 'C01010001'})
RETURN term;
```

### 전체 계층 구조 조회

```cypher
MATCH path = (root:Classification {level: 0})-[:PARENT_OF*0..]->(child:Classification)
RETURN path;
```

### 용어 검색

```cypher
MATCH (term:Term)
WHERE term.name_ko CONTAINS '금융'
RETURN term;
```

## 주의사항

- Memgraph에서 제약 조건 생성 시 기존 데이터가 있으면 오류 발생 가능
- 데이터 재적재 시 기존 데이터 삭제 필요:
  ```cypher
  MATCH (n) DETACH DELETE n;
  ```
