# https://school.programmers.co.kr/courses/13093/lessons/88779

from itertools import combinations

def solution(m, weights):
    answer = 0
    
    # 1개 부터 len(weights) 개까지 뽑는 조합
    for n in range(1, len(weights)):
        answer += [sum(w) for w in combinations(weights, n)].count(m)
        
    return answer
