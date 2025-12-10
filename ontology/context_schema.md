# context.json 스키마 설계

## 개요

context.json을 마스터 데이터로 두고, 이로부터 다음을 자동 생성:
- context.txt (사람이 읽기 편한 형식)
- mc_clsf.sql (분류 INSERT 문)
- mc_term.sql (용어 INSERT 문)
- memgraph.cypher (그래프 DB 쿼리)

## 데이터 흐름

```
context.json (마스터)
    ↓
generate.py
    ├→ context.txt
    ├→ mc_clsf.sql
    ├→ mc_term.sql
    └→ memgraph.cypher
```

## context.json 구조

```json
{
  "metadata": {
    "version": "1.0.0",
    "last_updated": "2024-11-30",
    "description": "MC 분류·용어 통합 체계"
  },
  "id_schema": {
    "classification": "C + DD(도메인) + LL(중분류) + SSSS(일련번호)",
    "term": "T + DD(도메인) + LL(중분류) + SSSS(일련번호)"
  },
  "constants": {
    "root_clsf_id": "03facd74b2d24f7cab807b8980391649",
    "root_term_id": "4147179070a84d3887b97eb57085d850"
  },
  "domains": [
    {
      "code": "01",
      "name_ko": "공공",
      "name_en": "Public Sector",
      "description": "공공 부문 정책 및 행정 전반",
      "classifications": [...],
      "terms": [...]
    }
  ]
}
```

### Classification 객체

```json
{
  "id": "C01010001",
  "name": "지방시대·지역균형발전",
  "description": "지방시대 정책과 지역균형발전을 다루는 분류",
  "readme": "중분류 01-01. 수도권 집중 완화, 지역 주도 발전, 인구감소지역 지원 정책 포함.",
  "group": true,
  "level": 1,
  "parent_id": "C01000001",
  "children": [
    {
      "id": "C01010002",
      "name": "인구감소지역·지방소멸 대응",
      "description": "인구감소지역 지원 및 지방소멸 대응 정책을 다루는 분류",
      "readme": "소분류. 인구감소지역 지원 특별법, 지방소멸대응기금 등 관련 정책.",
      "group": false,
      "level": 2,
      "parent_id": "C01010001",
      "children": []
    }
  ]
}
```

**필드 설명:**
- `id`: 분류 ID (C + 8자리)
- `name`: 분류명
- `description`: 분류 설명 (CLSF_DESC에 매핑)
- `readme`: 상세 설명 (README에 매핑)
- `group`: 그룹 여부 (GROUP_YN)
- `level`: 계층 레벨 (0: 도메인, 1: 중분류, 2: 소분류)
- `parent_id`: 상위 분류 ID
- `children`: 하위 분류 배열 (재귀 구조)

### Term 객체 (계층 구조 지원)

```json
{
  "id": "T07010001",
  "name_ko": "암",
  "name_en": "Cancer",
  "acronym": null,
  "description": "악성 종양으로, 비정상적인 세포의 무제한적인 성장과 전이를 특징으로 하는 질환",
  "linked_clsf_id": "C07010001",
  "parent_id": null,
  "children": [
    {
      "id": "T07010002",
      "name_ko": "대장암",
      "name_en": "Colorectal Cancer",
      "acronym": "CRC",
      "description": "대장(결장 및 직장)에 발생하는 악성 종양",
      "linked_clsf_id": "C07010001",
      "parent_id": "T07010001",
      "children": []
    },
    {
      "id": "T07010003",
      "name_ko": "다발성골수종",
      "name_en": "Multiple Myeloma",
      "acronym": "MM",
      "description": "골수의 형질세포에서 발생하는 혈액암",
      "linked_clsf_id": "C07010001",
      "parent_id": "T07010001",
      "children": []
    }
  ]
}
```

**필드 설명:**
- `id`: 용어 ID (T + 8자리)
- `name_ko`: 한글 용어명
- `name_en`: 영문 용어명
- `acronym`: 약어 (없으면 null)
- `description`: 용어 상세 설명 (TERM_DESC에 매핑)
- `linked_clsf_id`: 연결된 분류 ID (README에 매핑)
- `parent_id`: 상위 용어 ID (계층 구조)
- `children`: 하위 용어 배열 (재귀 구조)

## 계층 구조 예시

### 용어 계층 예시 1: 암 → 암 종류

```
T07010001 암 (Cancer)
├─ T07010002 대장암 (Colorectal Cancer)
└─ T07010003 다발성골수종 (Multiple Myeloma)
```

### 용어 계층 예시 2: 금융 → 세부 금융 개념

```
T02010001 기준금리 (Base Rate)
└─ T02010004 물가안정기 재진입 (Re-entry into Price Stability Phase)

T02010003 공개시장운영 (OMO)
├─ T02010007 통화안정증권 발행 (MSB Issuance)
└─ T02010008 환매조건부증권 매입 (RP Purchases)
```

### 용어 계층 예시 3: 이커머스 → 비즈니스 모델

```
T03010001 이커머스 (E-commerce)
├─ T03010003 D2C (Direct to Consumer)
├─ T03020001 라이브커머스 (Live Commerce)
└─ T03010004 구독경제 (Subscription Economy)
```

## 생성 규칙

### context.txt 생성
- 계층 구조를 트리 형식으로 표현
- 들여쓰기와 트리 기호(├, └, │) 사용

### SQL 생성
- **MC_CLSF**: parent_id로 계층 표현
- **MC_TERM**: PRT_TERM_ID로 계층 표현 (ROOT_TERM_ID 또는 상위 용어 ID)

### Cypher 생성
- **Classification**: PARENT_OF 관계
- **Term**: PARENT_OF 관계 (용어 간)
- **Term-Classification**: BELONGS_TO 관계

## 데이터 품질 규칙

1. **ID 유일성**: 모든 ID는 유일해야 함
2. **계층 일관성**: parent_id는 반드시 존재하는 ID여야 함
3. **순환 참조 금지**: A → B → A 같은 순환 불가
4. **설명 필수**: description 필드는 빈 문자열 불가
5. **분류 연결**: 모든 용어는 linked_clsf_id를 가져야 함

## 확장 가능성

향후 추가 가능한 필드:
- `synonyms`: 동의어 목록
- `related_terms`: 연관 용어 ID 목록
- `examples`: 사용 예시
- `references`: 참고 문헌
- `status`: active, deprecated, draft
- `tags`: 태그 목록
- `metadata`: 추가 메타데이터 (생성일, 수정일 등)
