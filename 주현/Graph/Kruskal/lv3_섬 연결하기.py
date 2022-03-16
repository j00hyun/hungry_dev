# https://programmers.co.kr/learn/courses/30/lessons/42861#

from collections import deque

# 크루스칼 알고리즘
def solution(n, costs):
    union_arr = [i for i in range(n)]
    costs = deque(sorted(costs, key=lambda x: x[2]))
    answer = 0
    
    # find
    def find(node):
        if union_arr[node] == node:
            return node
        
        union_arr[node] = find(union_arr[node])
        return union_arr[node]
    
    # 모든 섬이 연결될 때까지 작은 비용의 다리부터 연결
    while len(set([find(node) for node in range(n)])) > 1:
        a, b, cost = costs.popleft()
        small_root, big_root = sorted([find(a), find(b)])
        
        # union (큰 섬을 작은 섬 밑으로 연결)
        if small_root != big_root:
            union_arr[big_root] = small_root
            answer += cost
            
    return answer
