# https://school.programmers.co.kr/courses/13093/lessons/88758

from heapq import heapify, heappop, heappush

def solution(N, works):
    # 최대힙 구현하기 위해 - 부호 추가
    works = [-w for w in works]
    heapify(works)
    
    while N > 0:
        if works[0] == 0:
            break
            
        heappush(works, heappop(works) + 1)
        N -= 1
        
    return sum([w * w for w in works])
