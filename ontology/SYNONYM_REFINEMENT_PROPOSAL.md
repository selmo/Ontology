# 동의어 관계 세분화 제안

**작성일:** 2025-12-11
**버전:** 3.12.0 (제안)
**목적:** 동의어 관계를 SKOS 표준 기반으로 세분화

---

## 1. 현황 분석

### 현재 구조 (v3.11)
```json
{
  "synonyms": {
    "terms": ["T01010005"],        // Term → Term
    "strings": ["공기업", "공공단체"]  // 모두 "동의어"로 취급
  }
}
```

### 분석 결과 (465개 동의어)

| 유형 | 개수 | 비율 | 설명 |
|------|------|------|------|
| **완전 동의어** | 41 | 8.8% | 약어, 영문명 (OMO, DES, Cancer) |
| **파생어** | 16 | 3.4% | 접미사/접두사 추가 (교육복지 → 교육복지사업) |
| **상위 개념** | 12 | 2.6% | 더 일반적 (정부조직도 → 정부조직) |
| **하위 개념** | 40 | 8.6% | 더 구체적 (의료기관 → 보건의료기관) |
| **관련어** | 356 | **76.6%** | 관련성만 있음 (공공기관 → 공기업) |

**문제점:**
- 대부분(76.6%)이 실제로는 "관련어"이지 "동의어"가 아님
- 동의어와 관련어가 구분되지 않아 검색 정확도 저하
- 상하위 개념 관계가 동의어로 잘못 표현됨

---

## 2. SKOS 표준 기반 제안

### SKOS Mapping Properties

| SKOS 속성 | 의미 | 예시 |
|-----------|------|------|
| `skos:exactMatch` | 정확히 동일한 개념 | OMO ↔ 공개시장운영 |
| `skos:closeMatch` | 매우 유사한 개념 | 공기업 ↔ 공공기관 |
| `skos:relatedMatch` | 관련된 개념 | 공공기관 ↔ 공공단체 |
| `skos:broadMatch` | 상위 개념 | 정부조직 ← 정부조직도 |
| `skos:narrowMatch` | 하위 개념 | 의료기관 → 보건의료기관 |

### 제안 구조 (v3.12)

```json
{
  "synonyms": {
    "terms": ["T01010005"],           // Term → Term (기존 유지)
    "exact": ["OMO", "공개시장운영"],    // 완전 동의어
    "close": ["공기업"],               // 유사어
    "related": ["공공단체", "공공조직"],  // 관련어
    "broader": ["정부조직"],           // 상위 개념
    "narrower": ["보건의료기관"]        // 하위 개념
  }
}
```

---

## 3. 유형별 정의 및 예시

### 3.1 Exact Match (완전 동의어) - 41개

**정의:** 완전히 동일한 개념을 나타내는 다른 표현

**포함:**
- 약어 (OMO, DES, DC, DB, PF)
- 영문명 (Cancer, Performance, Exhibition)
- 한영 혼용 (IT자산, Big Data)

**예시:**
```
공개시장운영 → OMO
암 → Cancer
안구건조증 → DES (Dry Eye Syndrome)
```

**활용:** 검색 시 완전히 대체 가능

---

### 3.2 Close Match (유사어) - 자동 분류 안됨, 수동 분류 필요

**정의:** 의미가 매우 유사하지만 미묘한 차이가 있는 용어

**예시 (제안):**
```
공기업 ↔ 공공기관    (거의 같지만 법적 정의 다름)
지자체 ↔ 지방자치단체  (준말과 정식 명칭)
병원 ↔ 의료기관      (포함 관계이지만 흔히 혼용)
```

**활용:** 검색 시 우선순위를 약간 낮춰 함께 표시

---

### 3.3 Related Match (관련어) - 356개

**정의:** 관련성은 있지만 동의어나 상하위 개념이 아닌 용어

**예시:**
```
공공기관 → 공공단체, 공공조직
정부조직도 → 행정조직, 부처조직도
의료기관 → 병원, 보건의료기관
```

**활용:** "관련 검색어" 형태로 제시

---

### 3.4 Broad Match (상위 개념) - 12개

**정의:** 현재 용어보다 더 일반적이고 넓은 범위의 개념

**예시:**
```
정부조직도 → 정부조직 (상위)
교육통계연보 → 교육통계 (상위)
위식도역류질환 → 위식도역류 (상위)
```

**활용:** 계층적 탐색, 상위 범주로 확대 검색

---

### 3.5 Narrow Match (하위 개념) - 40개

**정의:** 현재 용어보다 더 구체적이고 좁은 범위의 개념

**예시:**
```
직업능력개발 → 직업능력개발훈련 (하위)
영재교육 → 영재교육원 (하위)
의료기관 → 보건의료기관 (하위)
약국 → 조제약국 (하위)
```

**활용:** 계층적 탐색, 하위 범주로 좁혀 검색

---

## 4. 데이터 모델 변경

### 4.1 ontology.json 스키마

**현재 (v3.11):**
```json
{
  "id": "T01010001",
  "name_ko": "공공기관",
  "synonyms": {
    "terms": [],
    "strings": ["공기업", "공공단체", "공공조직"]
  }
}
```

**제안 (v3.12):**
```json
{
  "id": "T01010001",
  "name_ko": "공공기관",
  "synonyms": {
    "terms": [],              // Term → Term (기존)
    "exact": [],              // 완전 동의어
    "close": ["공기업"],       // 유사어
    "related": ["공공단체", "공공조직"],  // 관련어
    "broader": [],            // 상위 개념
    "narrower": []            // 하위 개념
  }
}
```

### 4.2 Cypher 관계 타입

**제안:**
```cypher
// 1. Term → Term (기존 유지)
(t1:Term)-[:SYNONYM_OF]->(t2:Term)

// 2. Term → Synonym with type
(t:Term)-[:EXACT_SYNONYM]->(:Synonym {value: 'OMO'})
(t:Term)-[:CLOSE_SYNONYM]->(:Synonym {value: '공기업'})
(t:Term)-[:RELATED_SYNONYM]->(:Synonym {value: '공공단체'})
(t:Term)-[:BROADER_THAN]->(:Synonym {value: '정부조직'})
(t:Term)-[:NARROWER_THAN]->(:Synonym {value: '보건의료기관'})
```

**또는 단일 관계 타입 + 속성:**
```cypher
(t:Term)-[:SYNONYM_OF {type: 'exact'}]->(:Synonym {value: 'OMO'})
(t:Term)-[:SYNONYM_OF {type: 'close'}]->(:Synonym {value: '공기업'})
(t:Term)-[:SYNONYM_OF {type: 'related'}]->(:Synonym {value: '공공단체'})
```

### 4.3 SQL 스키마

**MC_TERM_REL 테이블 변경:**

**현재:**
```sql
REL_TYPE CHAR(1)  -- 'S': Synonym, 'T': Related Term
```

**제안:**
```sql
REL_TYPE VARCHAR(2)  -- 확장된 코드 체계
-- 'SE': Exact Synonym
-- 'SC': Close Synonym
-- 'SR': Related Synonym
-- 'SB': Broader (상위 개념)
-- 'SN': Narrower (하위 개념)
-- 'ST': Term (기존 'T' 유지)
```

---

## 5. 마이그레이션 전략

### Phase 1: 자동 분류 (1차)

**규칙 기반 자동 분류:**
- Exact: 약어, 영문명 (대문자, ASCII)
- Broader: 길이가 짧고 포함 관계
- Narrower: 길이가 길고 포함 관계
- Derived: 접미사/접두사 패턴
- Related: 나머지

**결과:**
- Exact: 41개
- Broader: 12개
- Narrower: 40개
- Derived: 16개 → Related로 분류
- Related: 356개

### Phase 2: 수동 검토 (2차)

**Close Match 식별:**
- Related로 분류된 356개 중 검토
- 의미적으로 매우 유사한 것을 Close로 재분류
- 예상 개수: 30~50개

**기준:**
- 일상적으로 혼용되는 용어
- 법적/기술적 차이만 있는 용어
- 준말과 정식 명칭 관계

### Phase 3: 검증

**자동 검증:**
- Exact: 대소문자만 다른지 확인
- Broader/Narrower: 상호 모순 확인
- Related: 다른 카테고리와 중복 확인

---

## 6. 구현 예시

### 6.1 마이그레이션 스크립트

```python
def migrate_synonyms_v312(term, synonym_str, categorized):
    """Migrate synonym to categorized structure"""

    term_id = term['id']
    term_name = term['name_ko']

    # Get category from analysis
    category = categorized.get(term_id, {}).get(synonym_str, 'related')

    # Initialize structure
    if 'synonyms_v312' not in term:
        term['synonyms_v312'] = {
            'terms': term.get('synonyms', {}).get('terms', []),
            'exact': [],
            'close': [],
            'related': [],
            'broader': [],
            'narrower': []
        }

    # Add to appropriate category
    term['synonyms_v312'][category].append(synonym_str)
```

### 6.2 검색 쿼리 예시

```cypher
// 정확도별 검색 (Exact > Close > Related)
MATCH (t:Term)
WHERE t.name_ko = '공공기관'
OPTIONAL MATCH (t)-[:EXACT_SYNONYM]->(e:Synonym)
OPTIONAL MATCH (t)-[:CLOSE_SYNONYM]->(c:Synonym)
OPTIONAL MATCH (t)-[:RELATED_SYNONYM]->(r:Synonym)
RETURN t.name_ko AS term,
       collect(DISTINCT e.value) AS exact_matches,
       collect(DISTINCT c.value) AS close_matches,
       collect(DISTINCT r.value) AS related_terms;
```

---

## 7. 기대 효과

### 7.1 검색 정확도 향상

**현재 (v3.11):**
- "공공기관" 검색 → "공기업", "공공단체", "공공조직" 모두 동일 가중치

**개선 (v3.12):**
- Exact: OMO, 공개시장운영 (100% 가중치)
- Close: 공기업 (90% 가중치)
- Related: 공공단체, 공공조직 (70% 가중치)

### 7.2 계층적 탐색 지원

```
[상위]
  정부조직
    ↓
[현재]
  정부조직도
    ↓
[하위]
  (없음)
```

### 7.3 SKOS 표준 호환

- RDF/OWL 변환 시 직접 매핑 가능
- 외부 온톨로지와 연계 용이
- 의미 웹(Semantic Web) 지원

---

## 8. 의사결정 사항

### A. 스키마 구조

**옵션 1: 단일 synonyms 객체 (권장)**
```json
"synonyms": {
  "terms": [...],
  "exact": [...],
  "close": [...],
  "related": [...],
  "broader": [...],
  "narrower": [...]
}
```

**옵션 2: 별도 필드**
```json
"synonyms": {...},
"exact_synonyms": [...],
"close_synonyms": [...],
...
```

### B. Cypher 관계 타입

**옵션 1: 타입별 관계 (권장)**
- `:EXACT_SYNONYM`, `:CLOSE_SYNONYM`, `:RELATED_SYNONYM`
- 장점: 타입별 쿼리 효율
- 단점: 관계 타입 증가

**옵션 2: 속성으로 구분**
- `:SYNONYM_OF {type: 'exact'}`
- 장점: 단일 관계 타입
- 단점: 필터링 필요

### C. Close Match 식별 방법

**옵션 1: 자동 + 수동**
- 1차 자동 분류 → 2차 수동 검토
- 권장

**옵션 2: 완전 수동**
- 모든 Related를 수동 검토
- 시간 소요

### D. 마이그레이션 시점

**옵션 1: 단계적 (권장)**
- v3.12: 자동 분류만 적용
- v3.13: 수동 검토 완료

**옵션 2: 일괄**
- v3.12: 모두 완료
- 시간 필요

---

## 9. 다음 단계

1. **의사결정 확인** (A, B, C, D)
2. **자동 분류 스크립트 작성**
3. **ontology.json 업데이트**
4. **generate.py 수정**
5. **검증 및 테스트**
6. **수동 검토 (Close Match)**
7. **v3.12 릴리스**

---

## 10. 참고 자료

- **SKOS Primer**: https://www.w3.org/TR/skos-primer/
- **ISO 25964**: Thesauri and interoperability with other vocabularies
- **synonym_categories.json**: 자동 분류 결과
- **analyze_synonym_types.py**: 분석 스크립트
