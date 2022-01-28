# https://programmers.co.kr/learn/courses/30/lessons/12978

import sys
import heapq
from collections import defaultdict

def solution(N, road, K):
    # 다익스트라 알고리즘 기본 함수
    def dijkstra(graph, start):
        result = {node: sys.maxsize for node in graph}
        result[start] = 0
        heap = []
        heapq.heappush(heap, [result[start], start])
        
        while heap:
            cur_dist, cur_dest = heapq.heappop(heap)
            
            if result[cur_dest] < cur_dist:
                continue
            
            for next_dest, next_dist in graph[cur_dest].items():
                dist = cur_dist + next_dist
                
                if dist < result[next_dest]:
                    result[next_dest] = dist
                    heapq.heappush(heap, [dist, next_dest])
                    
        return result
    
    graph = {n: {} for n in range(1, N + 1)}
    answer = 0
    
    for st, dt, n in road:
        # 테스트케이스 2: 3-5 사이 처럼 도로가 2개 이상 있는 경우 가장 적은 시간 저장
        if graph[st].get(dt) is not None and graph[st][dt] < n:
            continue
        graph[st][dt] = n
        graph[dt][st] = n
        
    shortest = dijkstra(graph, 1)
    
    for _, n in shortest.items():
        if n <= K:
            answer += 1
            
    return answer
