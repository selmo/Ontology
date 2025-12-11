# 타입별 동의어 검색 최적화 가이드

**버전:** v3.13.3
**작성일:** 2025-12-11
**목적:** SKOS 기반 동의어 타입별 검색 우선순위 및 가중치 시스템 활용

---

## 개요

v3.12에서 도입된 **SKOS 기반 5가지 동의어 타입**을 활용한 검색 최적화 시스템입니다.
동의어 타입별로 **가중치**를 부여하여 검색 정확도를 향상시킵니다.

### 동의어 타입 및 가중치

| 타입 | 코드 | 가중치 | 설명 | 예시 |
|------|------|--------|------|------|
| **Exact Synonym** | SE | 1.0 | 완전 동의어 | IT ↔ 정보기술 |
| **Close Synonym** | SC | 0.9 | 유사어 | 공기업 ↔ 공공기관 |
| **Term Synonym** | S | 0.8 | 용어간 동의어 | T01010001 ↔ T01010005 |
| **Related Synonym** | SR | 0.7 | 관련어 | 공공기관 ↔ 공공기관정보 |
| **Broader** | SB | 0.6 | 상위 개념 | 동물 ← 포유류 |
| **Narrower** | SN | 0.6 | 하위 개념 | 포유류 → 동물 |

---

## 검색 우선순위

1. **Exact Name Match** (1.0) - 용어명 정확 일치
2. **Exact Synonym** (1.0) - 완전 동의어 일치
3. **Close Synonym** (0.9) - 유사어 일치
4. **Term Synonym** (0.8) - 용어간 동의어
5. **Related Synonym** (0.7) - 관련어 일치
6. **Broader/Narrower** (0.6) - 계층 관계

---

## 사용법

### Python API

```python
from synonym_search_optimization import SynonymSearchOptimizer

# 초기화
optimizer = SynonymSearchOptimizer('ontology.json')

# 검색
results = optimizer.search("공기업", max_results=10)

# 결과 출력
for result in results:
    print(f"{result['term_name']}: {result['score']:.0f}점 ({result['match_type']})")
```

### 통계 조회

```python
stats = optimizer.get_synonym_statistics()
print(f"총 용어: {stats['total_terms']}개")
print(f"총 동의어: {stats['total_synonyms']}개")
print(f"타입별 분포: {stats['synonym_types']}")
```

---

## 샘플 쿼리

### 1. Exact Synonym 검색 (가중치 1.0)

**쿼리:** "IT"

```
결과:
1. 정보기술 (100점, synonym_exact)
   - 설명: IT는 정보기술의 완전한 동의어
   - 매치 타입: Exact Synonym
```

**쿼리:** "ICT"

```
결과:
1. 정보기술 (100점, synonym_exact)
   - 설명: ICT(Information and Communication Technology)는 IT의 확장 개념으로 완전 동의어
   - 매치 타입: Exact Synonym
```

**쿼리:** "AI"

```
결과:
1. 인공지능 (100점, synonym_exact)
   - 설명: AI는 Artificial Intelligence의 약어
   - 매치 타입: Exact Synonym
```

---

### 2. Close Synonym 검색 (가중치 0.9)

**쿼리:** "공기업"

```
결과:
1. 공공기관 (90점, synonym_close)
   - 설명: 공기업은 공공기관의 하위 유형으로 밀접한 관계
   - 매치 타입: Close Synonym
```

**쿼리:** "공공단체"

```
결과:
1. 공공기관 (90점, synonym_close)
   - 설명: 공공단체는 공공기관의 유사 용어
   - 매치 타입: Close Synonym
```

**쿼리:** "지자체"

```
결과:
1. 지방자치단체 (90점, synonym_close)
   - 설명: 지자체는 지방자치단체의 약칭
   - 매치 타입: Close Synonym
```

**쿼리:** "행정센터"

```
결과:
1. 행정복지센터 (90점, synonym_close)
   - 설명: 행정센터는 행정복지센터의 줄임말 (구 동사무소)
   - 매치 타입: Close Synonym
```

**쿼리:** "국민서비스"

```
결과:
1. 대민서비스 (90점, synonym_close)
   - 설명: 국민서비스는 대민서비스의 유사 표현
   - 매치 타입: Close Synonym
```

**쿼리:** "판결례"

```
결과:
1. 판례 (90점, synonym_close)
   - 설명: 판결례는 판례의 법률 용어 변형
   - 매치 타입: Close Synonym
```

---

### 3. Related Synonym 검색 (가중치 0.7)

**쿼리:** "공공기관정보"

```
결과:
1. 공공기관 (70점, synonym_related)
   - 설명: 공공기관정보는 공공기관의 관련 정보를 지칭
   - 매치 타입: Related Synonym
```

**쿼리:** "기관현황"

```
결과:
1. 공공기관 (70점, synonym_related)
   - 설명: 기관현황은 공공기관의 현황 데이터
   - 매치 타입: Related Synonym
```

**쿼리:** "법령정보"

```
결과:
1. 법령 (70점, synonym_related)
   - 설명: 법령정보는 법령의 관련 정보
   - 매치 타입: Related Synonym
```

---

### 4. 복합 검색 (여러 타입 혼합)

**쿼리:** "정보통신기술"

```
결과:
1. 정보기술 (90점, synonym_close)
   - 설명: 정보통신기술(ICT)은 정보기술(IT)의 확장 개념
   - 매치 타입: Close Synonym
```

**쿼리:** "통화금융정책"

```
결과:
1. 통화정책 (90점, synonym_close)
   - 설명: 통화금융정책은 통화정책의 확장 표현
   - 매치 타입: Close Synonym
```

**쿼리:** "재무상태표"

```
결과:
1. 재정상태표 (90점, synonym_close)
   - 설명: 재무상태표는 회계 용어로 재정상태표와 유사
   - 매치 타입: Close Synonym
```

---

## 검색 점수 계산

### 점수 산정 방식

```
점수 = 가중치 × 100
```

### 예시

| 검색어 | 매칭 타입 | 가중치 | 점수 |
|--------|-----------|--------|------|
| "IT" → 정보기술 | Exact Synonym | 1.0 | 100 |
| "공기업" → 공공기관 | Close Synonym | 0.9 | 90 |
| "기관현황" → 공공기관 | Related Synonym | 0.7 | 70 |

---

## 검색 정확도 향상 사례

### Before (v3.11 이전 - 단일 SYNONYM)

```python
# 모든 동의어가 동일한 우선순위
search("IT") → 정보기술 (동의어)
search("공기업") → 공공기관 (동의어)
search("기관현황") → 공공기관 (동의어)
# 모두 동일한 가중치로 반환됨 → 정확도 구분 불가
```

### After (v3.12+ - 타입별 SYNONYM)

```python
# 타입별 우선순위 적용
search("IT") → 정보기술 (100점, Exact)
search("공기업") → 공공기관 (90점, Close)
search("기관현황") → 공공기관 (70점, Related)
# 명확한 우선순위로 검색 정확도 향상
```

---

## 통계 (v3.13.3)

### 전체 동의어 분포

```
총 용어: 401개
총 동의어: 519개

타입별 분포:
- Exact Synonym: 41개 (가중치 1.0)
- Close Synonym: 74개 (가중치 0.9)
- Term Synonym: 5개 (가중치 0.8)
- Related Synonym: 347개 (가중치 0.7)
- Broader: 12개 (가중치 0.6)
- Narrower: 40개 (가중치 0.6)
```

### 커버리지

```
동의어 보유 용어: 221개 / 401개 (55.1%)
평균 동의어 수: 2.3개/용어
최대 동의어 수: 8개 (T01010001 공공기관)
```

---

## 활용 시나리오

### 1. 검색 엔진 통합

```python
def search_terms(user_query):
    optimizer = SynonymSearchOptimizer()
    results = optimizer.search(user_query, max_results=5)

    # Exact/Close만 상위 노출 (점수 85+ 필터링)
    high_confidence = [r for r in results if r['score'] >= 85]

    return high_confidence
```

### 2. 자동 태깅 시스템

```python
def auto_tag(document_text):
    optimizer = SynonymSearchOptimizer()
    tags = []

    for word in extract_keywords(document_text):
        results = optimizer.search(word)
        if results and results[0]['score'] >= 90:  # Close 이상만
            tags.append(results[0]['term_name'])

    return tags
```

### 3. 용어 추천 시스템

```python
def suggest_standard_term(user_input):
    optimizer = SynonymSearchOptimizer()
    results = optimizer.search(user_input, max_results=3)

    if results:
        best_match = results[0]
        if best_match['score'] >= 90:
            return f"추천: '{best_match['term_name']}' (정확도: {best_match['score']:.0f}%)"

    return "표준 용어 없음"
```

---

## 성능 최적화

### 인덱싱 전략

```python
# 3-tier 인덱스 구조
term_index = {}      # term_id → term data (O(1) lookup)
name_index = {}      # term_name (lower) → term_id (O(1) lookup)
synonym_index = {}   # synonym (lower) → [(term_id, type, weight)] (O(1) lookup)
```

### 검색 복잡도

- **시간 복잡도:** O(1) - 해시 인덱스 기반
- **공간 복잡도:** O(n) - n = 용어 수 + 동의어 수

### 대용량 처리

```python
# 대용량 배치 검색
queries = ["IT", "공기업", "지자체", ...]
results = [optimizer.search(q) for q in queries]
# 1,000개 쿼리 처리: ~0.5초 (인덱스 기반)
```

---

## 참고 자료

- **SKOS 표준:** https://www.w3.org/2004/02/skos/
- **ISO 25964:** https://www.iso.org/standard/53657.html
- **ontology.json:** 마스터 데이터 파일
- **SYNONYM_REFINEMENT_PROPOSAL.md:** v3.12 타입 세분화 설계 문서

---

## 변경 이력

- **v3.13.3** (2025-12-11): 검색 최적화 가이드 작성
- **v3.13.1** (2025-12-11): Close Match 48개 추가 (0.85+)
- **v3.13.2** (2025-12-11): Close Match 8개 추가 (안전 패턴)
- **v3.13.3** (2025-12-11): Close Match 12개 추가 (수동 검토)
- **v3.12.0** (2025-12-11): SKOS 기반 타입 세분화 도입

---

## 문의

기술 문의 또는 개선 제안은 프로젝트 저장소의 이슈로 등록해주세요.
