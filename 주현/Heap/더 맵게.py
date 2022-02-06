# https://programmers.co.kr/learn/courses/30/lessons/42626

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K:
        try:
            heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
            answer += 1

        except IndexError:
            return -1
    
    return answer
