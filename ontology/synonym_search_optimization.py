#!/usr/bin/env python3
"""
타입별 동의어 검색 최적화 시스템

SKOS 기반 동의어 타입에 따른 검색 우선순위 및 가중치 적용
"""

import json
from typing import List, Dict, Tuple


class SynonymSearchOptimizer:
    """
    동의어 검색 최적화 클래스
    
    검색 우선순위 (SKOS 기반):
    1. Exact Match (1.0) - 완전 동의어
    2. Close Match (0.9) - 유사어
    3. Related Match (0.7) - 관련어
    4. Broader Match (0.6) - 상위 개념
    5. Narrower Match (0.6) - 하위 개념
    6. Term→Term (0.8) - 용어간 동의어
    """
    
    # 타입별 가중치
    WEIGHTS = {
        'exact': 1.0,
        'close': 0.9,
        'term': 0.8,
        'related': 0.7,
        'broader': 0.6,
        'narrower': 0.6
    }
    
    # 검색 우선순위 (높은 것부터)
    PRIORITY_ORDER = ['exact', 'close', 'term', 'related', 'broader', 'narrower']
    
    def __init__(self, ontology_file='ontology.json'):
        """온톨로지 파일 로드"""
        with open(ontology_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        # Build indexes
        self._build_indexes()
    
    def _build_indexes(self):
        """검색을 위한 인덱스 구축"""
        self.term_index = {}  # term_id -> term data
        self.name_index = {}  # term_name (lower) -> term_id
        self.synonym_index = {}  # synonym (lower) -> [(term_id, syn_type, weight)]
        
        for domain in self.data['domains']:
            for term in domain.get('terms', []):
                term_id = term['id']
                term_name = term['name_ko'].lower()
                
                # Term index
                self.term_index[term_id] = term
                
                # Name index
                self.name_index[term_name] = term_id
                
                # Synonym index
                synonyms = term.get('synonyms', {})
                if isinstance(synonyms, dict):
                    # Term→Term synonyms
                    for syn_term_id in synonyms.get('terms', []):
                        if syn_term_id in self.term_index:
                            syn_name = self.term_index[syn_term_id]['name_ko'].lower()
                            if syn_name not in self.synonym_index:
                                self.synonym_index[syn_name] = []
                            self.synonym_index[syn_name].append((
                                term_id, 'term', self.WEIGHTS['term']
                            ))
                    
                    # String synonyms by type
                    for syn_type in ['exact', 'close', 'related', 'broader', 'narrower']:
                        for syn_str in synonyms.get(syn_type, []):
                            syn_lower = syn_str.lower()
                            if syn_lower not in self.synonym_index:
                                self.synonym_index[syn_lower] = []
                            self.synonym_index[syn_lower].append((
                                term_id, syn_type, self.WEIGHTS[syn_type]
                            ))
    
    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        검색어에 대한 최적화된 검색
        
        Args:
            query: 검색어
            max_results: 최대 결과 수
        
        Returns:
            검색 결과 리스트 (정렬됨, 높은 점수부터)
        """
        query_lower = query.lower()
        results = []
        
        # 1. Exact term name match (highest priority)
        if query_lower in self.name_index:
            term_id = self.name_index[query_lower]
            term = self.term_index[term_id]
            results.append({
                'term_id': term_id,
                'term_name': term['name_ko'],
                'match_type': 'exact_name',
                'weight': 1.0,
                'score': 100.0
            })
        
        # 2. Synonym matches (with type-based weighting)
        if query_lower in self.synonym_index:
            for term_id, syn_type, weight in self.synonym_index[query_lower]:
                term = self.term_index[term_id]
                
                # Calculate score based on weight
                score = weight * 100
                
                results.append({
                    'term_id': term_id,
                    'term_name': term['name_ko'],
                    'match_type': f'synonym_{syn_type}',
                    'weight': weight,
                    'score': score
                })
        
        # Sort by score (descending)
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return results[:max_results]
    
    def get_synonym_statistics(self) -> Dict:
        """동의어 통계 반환"""
        stats = {
            'total_terms': len(self.term_index),
            'synonym_types': {
                'exact': 0,
                'close': 0,
                'related': 0,
                'broader': 0,
                'narrower': 0,
                'term': 0
            },
            'total_synonyms': 0
        }
        
        for term in self.term_index.values():
            synonyms = term.get('synonyms', {})
            if isinstance(synonyms, dict):
                for syn_type in stats['synonym_types'].keys():
                    count = len(synonyms.get(syn_type if syn_type != 'term' else 'terms', []))
                    stats['synonym_types'][syn_type] += count
                    stats['total_synonyms'] += count
        
        return stats


def demo_search():
    """검색 데모"""
    print("=== 타입별 동의어 검색 최적화 데모 ===\n")
    
    optimizer = SynonymSearchOptimizer()
    
    # Statistics
    stats = optimizer.get_synonym_statistics()
    print(f"총 용어: {stats['total_terms']}개")
    print(f"총 동의어: {stats['total_synonyms']}개\n")
    print("타입별 분포:")
    for syn_type, count in stats['synonym_types'].items():
        weight = optimizer.WEIGHTS[syn_type]
        print(f"  {syn_type:10s}: {count:3d}개 (가중치: {weight:.1f})")
    
    # Demo searches
    test_queries = [
        "공공기관",
        "공기업",  # Exact synonym of 공공기관
        "공공단체",  # Close synonym of 공공기관
        "IT",  # Exact synonym
        "ICT",  # Close synonym
        "지자체",  # Close synonym of 지방자치단체
    ]
    
    print("\n=== 검색 데모 ===\n")
    for query in test_queries:
        results = optimizer.search(query)
        print(f"검색어: '{query}'")
        if results:
            for i, result in enumerate(results[:3], 1):
                print(f"  {i}. {result['term_name']} "
                      f"(타입: {result['match_type']}, "
                      f"가중치: {result['weight']:.1f}, "
                      f"점수: {result['score']:.0f})")
        else:
            print("  결과 없음")
        print()


if __name__ == '__main__':
    demo_search()
