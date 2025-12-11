# 용어 관계 재구조화 제안

**작성일:** 2025-12-01
**버전:** v3.11 (제안)
**목적:** SYNONYM 및 RELATED_TO 관계 관리 정책 수립

---

## 1. 현재 구조 분석

### 현재 SYNONYM_OF 구조
```cypher
(:Term)-[:SYNONYM_OF]->(:Synonym)
```

**특징:**
- Synonym을 별도 노드로 생성
- Synonym은 단순 문자열 값 (value 속성)
- Term과 Synonym 간 1:N 관계

**예시:**
```cypher
MATCH (t:Term {id: 'T01010001', name_ko: '공공기관'})
CREATE (t)-[:SYNONYM_OF]->(:Synonym {value: '공기업'});
CREATE (t)-[:SYNONYM_OF]->(:Synonym {value: '공공단체'});
```

### 문제점

**Case 1: 동의어가 다른 TERM으로 존재하는 경우**
```
T01010001 공공기관
  synonyms: ['공기업', '공공단체']

T01010005 공기업 (별도 Term으로 존재)
  definition: "국가 또는 지방자치단체가 직접 운영하는 기업"
```

현재 구조에서는:
- '공기업'이 Synonym 노드로 존재
- '공기업'이 Term 노드로도 존재
- 두 개체 간 연결 없음 → 데이터 중복 및 불일치

**Case 2: 동의어가 TERM이 아닌 경우**
```
T01010001 공공기관
  synonyms: ['공공단체']

'공공단체'는 별도 Term으로 정의되지 않음
```

현재 구조로 적합함:
- Synonym 노드로만 존재
- Term과 명확히 구분됨

---

## 2. 제안: 하이브리드 SYNONYM 관리 정책

### 정책 원칙

1. **SYNONYM이 다른 TERM으로 존재하는 경우**
   - `Term → Term` 관계 사용
   - 관계 타입: `SYNONYM_OF`
   - 양방향(bidirectional) 관계
   - Synonym 노드 생성하지 않음

2. **SYNONYM이 TERM이 아닌 경우**
   - `Term → Synonym` 노드 관계 유지
   - 현재 구조 그대로 사용

### 데이터 구조

#### Schema 1: Term → Term (동의어가 Term인 경우)
```cypher
(:Term {id: 'T01010001', name_ko: '공공기관'})-[:SYNONYM_OF]->(:Term {id: 'T01010005', name_ko: '공기업'})
(:Term {id: 'T01010005', name_ko: '공기업'})-[:SYNONYM_OF]->(:Term {id: 'T01010001', name_ko: '공공기관'})
```

**속성:**
- 양방향 관계 (쿼리 편의성)
- Term 노드 재사용
- 데이터 중복 없음

#### Schema 2: Term → Synonym Node (동의어가 단순 문자열인 경우)
```cypher
(:Term {id: 'T01010001', name_ko: '공공기관'})-[:SYNONYM_OF]->(:Synonym {value: '공공단체'})
```

**속성:**
- 단방향 관계
- Synonym 노드 생성
- 가볍고 유연함

---

## 3. ontology.json 스키마 변경

### 현재 구조
```json
{
  "id": "T01010001",
  "name_ko": "공공기관",
  "synonyms": ["공기업", "공공단체"]
}
```

### 제안 구조 (v3.11)
```json
{
  "id": "T01010001",
  "name_ko": "공공기관",
  "synonyms": {
    "terms": ["T01010005"],      // TERM ID 참조
    "strings": ["공공단체"]       // 단순 문자열
  }
}
```

**또는 간소화된 구조:**
```json
{
  "id": "T01010001",
  "name_ko": "공공기관",
  "synonym_terms": ["T01010005"],    // Term → Term
  "synonym_strings": ["공공단체"]    // Term → Synonym node
}
```

---

## 4. RELATED_TO 관계 재정의

### 현재 문제 (v3.10에서 잘못된 제거)
- 모든 RELATED_TO 관계가 제거됨 (79개)
- 실제로는 조건부 제거가 필요함

### 제거 조건

**RELATED_TO를 제거해야 하는 경우:**

```python
# Case 1: PARENT_OF 관계가 존재하는 경우
T01010001 (부모) -[:PARENT_OF]-> T01010002 (자식)
# 이 경우 T01010001 -[:RELATED_TO]-> T01010002는 중복

# Case 2: SYNONYM_OF 관계가 존재하는 경우
T01010001 -[:SYNONYM_OF]-> T01010005
# 이 경우 T01010001 -[:RELATED_TO]-> T01010005는 중복
```

**RELATED_TO를 유지해야 하는 경우:**

```python
# 계층 관계도 동의어 관계도 아닌 순수 연관 관계
T03010001 (의료기관) -[:RELATED_TO]-> T03020001 (의료이용)
# 두 용어는 부모-자식도 아니고 동의어도 아니지만 의미적으로 연관됨
```

### 제거 알고리즘

```python
def should_keep_related_to(term1_id, term2_id, ontology_data):
    """
    RELATED_TO 관계를 유지할지 판단

    Returns:
        True: 유지 (다른 관계 없음)
        False: 제거 (PARENT_OF 또는 SYNONYM_OF 존재)
    """
    # Check PARENT_OF
    if has_parent_child_relation(term1_id, term2_id):
        return False

    # Check SYNONYM_OF (Term → Term)
    if has_synonym_relation(term1_id, term2_id):
        return False

    # 다른 관계가 없으면 RELATED_TO 유지
    return True
```

---

## 5. 구현 계획

### Phase 1: SYNONYM 재구조화

**Step 1.1: ontology.json 분석**
- 모든 Term의 synonyms 필드 검사
- synonym 문자열이 다른 Term의 name_ko와 일치하는지 확인
- Term ID 매핑 생성

**Step 1.2: ontology.json 업데이트**
```python
# Before
"synonyms": ["공기업", "공공단체"]

# After
"synonym_terms": ["T01010005"],    # '공기업'이 T01010005로 존재
"synonym_strings": ["공공단체"]    # '공공단체'는 Term 아님
```

**Step 1.3: generate.py 수정**
- SYNONYM_OF: Term → Term 생성 로직 추가
- SYNONYM_OF: Term → Synonym node 생성 로직 유지
- 양방향 관계 생성 (Term → Term의 경우)

### Phase 2: RELATED_TO 조건부 복원

**Step 2.1: v3.9 백업에서 RELATED_TO 복원**
- v3.10 이전 상태의 related_terms 필드 복원

**Step 2.2: 중복 관계 제거 로직 적용**
```python
for term in all_terms:
    if 'related_terms' in term:
        filtered_related = []
        for rel_id in term['related_terms']:
            # PARENT_OF 체크
            if rel_id == term.get('parent_id'):
                continue  # 제거

            # SYNONYM_OF 체크
            if rel_id in term.get('synonym_terms', []):
                continue  # 제거

            # 유지
            filtered_related.append(rel_id)

        term['related_terms'] = filtered_related
```

### Phase 3: 검증 및 문서화

**Step 3.1: validate_ontology.py 업데이트**
- SYNONYM_OF 양방향 체크 (Term → Term의 경우)
- RELATED_TO 중복 체크 (PARENT_OF, SYNONYM_OF와 중복 여부)

**Step 3.2: README.md 업데이트**
- 새로운 관계 구조 문서화
- Cypher 쿼리 예시 추가

---

## 6. 관계 타입 정리 (v3.11 제안)

### 최종 관계 구조

| 관계 타입 | Source | Target | 설명 | 방향성 | 개수 (예상) |
|----------|--------|--------|------|--------|------------|
| PARENT_OF | Classification | Classification | 분류 계층 | 단방향 | 376 |
| PARENT_OF | Term | Term | 용어 계층 | 단방향 | 221 |
| BELONGS_TO | Term | Classification | 용어 소속 | 단방향 | 221 |
| SYNONYM_OF | Term | Term | 동의어 (Term) | 양방향 | ~20 |
| SYNONYM_OF | Term | Synonym | 동의어 (문자열) | 단방향 | ~532 |
| RELATED_TO | Term | Term | 연관 관계 | 양방향 | ~60 |
| SIMILAR_TO | Classification | Classification | 유사 분류 | 양방향 | 42 |

**총 관계 수:** ~1,472 (v3.10: 1,453)

### Cypher 쿼리 예시

```cypher
-- 1. Term의 모든 동의어 찾기 (하이브리드)
MATCH (t:Term {id: 'T01010001'})
OPTIONAL MATCH (t)-[:SYNONYM_OF]->(syn_term:Term)
OPTIONAL MATCH (t)-[:SYNONYM_OF]->(syn_node:Synonym)
RETURN t.name_ko AS term,
       collect(DISTINCT syn_term.name_ko) AS synonym_terms,
       collect(DISTINCT syn_node.value) AS synonym_strings;

-- 2. 순수 연관 관계만 찾기 (PARENT_OF, SYNONYM_OF 제외)
MATCH (t1:Term)-[:RELATED_TO]->(t2:Term)
WHERE NOT (t1)-[:PARENT_OF]-(t2)
  AND NOT (t1)-[:SYNONYM_OF]-(t2)
RETURN t1.name_ko, t2.name_ko;

-- 3. 유사 분류 찾기
MATCH (c1:Classification)-[:SIMILAR_TO]->(c2:Classification)
WHERE c1.id < c2.id  -- 중복 제거
RETURN c1.name AS classification1, c2.name AS classification2;
```

---

## 7. 마이그레이션 체크리스트

### 사전 준비
- [ ] v3.10 백업 생성 (현재 상태)
- [ ] v3.9 백업 확인 (RELATED_TO 복원용)

### SYNONYM 재구조화
- [ ] ontology.json에서 synonym 문자열 분석
- [ ] Term 매핑 테이블 생성 (synonym string → Term ID)
- [ ] ontology.json 스키마 변경 (synonym_terms, synonym_strings)
- [ ] generate.py 수정 (Term → Term SYNONYM_OF 추가)
- [ ] 양방향 관계 생성 로직 추가

### RELATED_TO 복원
- [ ] v3.9에서 related_terms 복원
- [ ] 중복 제거 로직 구현 (PARENT_OF, SYNONYM_OF 체크)
- [ ] 필터링된 related_terms를 ontology.json에 적용

### 검증
- [ ] validate_ontology.py 실행 (0 errors, 0 warnings)
- [ ] Cypher 파일 생성 확인
- [ ] SQL 파일 생성 확인
- [ ] 관계 수 통계 확인

### 문서화
- [ ] README.md 업데이트
- [ ] CHANGELOG 작성
- [ ] Git commit (v3.11)

---

## 8. 의사결정 필요 사항

### A. SYNONYM 스키마 선택

**옵션 1: 구조화된 객체**
```json
"synonyms": {
  "terms": ["T01010005"],
  "strings": ["공공단체"]
}
```
- 장점: 명확한 구분
- 단점: 스키마 복잡도 증가

**옵션 2: 별도 필드**
```json
"synonym_terms": ["T01010005"],
"synonym_strings": ["공공단체"]
```
- 장점: 간단하고 명확
- 단점: 필드 수 증가

**권장:** 옵션 2 (별도 필드)

### B. SYNONYM_OF 양방향 생성 방식

**옵션 1: 자동 양방향 생성**
```python
# Term A → Term B 정의 시 자동으로 B → A 생성
if term_a.synonym_terms = [term_b_id]:
    # Generate both directions
    CREATE (a)-[:SYNONYM_OF]->(b)
    CREATE (b)-[:SYNONYM_OF]->(a)
```

**옵션 2: 명시적 정의**
```python
# 양쪽 모두 명시적으로 정의 필요
term_a.synonym_terms = [term_b_id]
term_b.synonym_terms = [term_a_id]
```

**권장:** 옵션 1 (자동 양방향)

### C. RELATED_TO 필터링 적용 시점

**옵션 1: ontology.json 업데이트 시 적용**
- 마스터 파일에 이미 필터링된 관계만 저장
- 장점: 데이터 일관성
- 단점: 원본 정보 손실

**옵션 2: 생성 스크립트에서 동적 필터링**
- ontology.json에는 모든 related_terms 유지
- generate.py에서 Cypher/SQL 생성 시 필터링
- 장점: 원본 정보 보존
- 단점: 복잡도 증가

**권장:** 옵션 1 (마스터 파일에서 필터링)

---

## 9. 예상 영향

### 데이터 변경
- **SYNONYM_OF (Term → Term)**: 0 → ~20개 (추정)
- **SYNONYM_OF (Term → Synonym)**: 552 → ~532개 (추정)
- **RELATED_TO**: 0 (v3.10) → ~60개 (복원 후 필터링)

### 파일 크기
- `ontology.json`: 약간 증가 (synonym 필드 구조화)
- `generated/ontology.cypher`: 약간 증가 (양방향 관계)

### 쿼리 성능
- SYNONYM 조회: 개선 (Term → Term 직접 참조)
- RELATED_TO 조회: 개선 (중복 관계 제거)

---

## 10. 다음 단계

1. **의사결정 확인**
   - 위 8절의 옵션 A, B, C 선택

2. **구현 시작**
   - Phase 1부터 순차 진행

3. **테스트 및 검증**
   - 각 Phase 완료 후 검증

4. **v3.11 릴리스**
   - 모든 검증 통과 후 commit

---

**검토 요청:**
- [ ] SYNONYM 하이브리드 정책 승인
- [ ] RELATED_TO 필터링 조건 승인
- [ ] 스키마 옵션 선택 (8절)
- [ ] 구현 시작 승인
