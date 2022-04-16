# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations
from collections import Counter

def solution(relation):
    column = len(relation[0]) # column 갯수 
    candidate_keys = set() # 후보키
    
    # 유일성 검사
    def is_uniqueness(values):
        value_count = Counter(map(tuple, values))
        for i in value_count.values():
            if i != 1:
                return False
        return True
    
    # 최소성 검사
    def is_minimality(keys):
        for length in range(1, len(keys)):
            for sub_key in combinations(keys, length):
                if sub_key in candidate_keys:
                    return False
        return True
    
    
    for key_len in range(1, column + 1):
        
        # column에서 가능한 조합들 차례대로
        for keys in combinations(range(column), key_len):
            
            # 조합에 해당하는 column value값 저장
            values = [[] for _ in range(len(relation))]
            for key in keys:
                for row, value in enumerate(relation):
                    values[row].append(value[key])
            
            # 유일성, 최소성 만족 시 후보키에 등록
            if is_uniqueness(values) and is_minimality(keys):
                candidate_keys.add(keys)

    return len(candidate_keys)
