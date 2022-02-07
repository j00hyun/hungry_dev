# https://programmers.co.kr/learn/courses/30/lessons/12927

from heapq import heapify, heappush, heappop

def solution(n, works):
    works = [-w for w in works]
    heapify(works)
    
    for _ in range(n):
        
        # 남아있는 일이 없다면 끝냄
        if works[0] == 0:
            break
        
        # 작업량이 가장 큰 일을 선택
        heappush(works, heappop(works) + 1)
        
    return sum(w ** 2 for w in works)
