# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

# 댜익스트라..? bfs같은 느낌 -> 비용이 없을경우는 bfs가 더 효율적?
def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [0] * (n + 1)
    is_visited = [True if node < 2 else False for node in range(n + 1)]
    queue = deque([1])
    
    # 간선정보 연결리스트화
    for from_node, to_node in edge:
        graph[from_node].append(to_node)
        graph[to_node].append(from_node)
        
    while queue:
        curr_node = queue.popleft()
        
        for next_node in graph[curr_node]:
            # 비용이 존재하지 않으므로 이전에 방문했던 곳은 무조건 비용이 더 적음
            if is_visited[next_node] is False:
                is_visited[next_node] = True
                distance[next_node] = distance[curr_node] + 1
                queue.append(next_node)
    
    # 최단거리 중 가장 긴 거리인 노드 개수 반환
    return distance.count(max(distance))
