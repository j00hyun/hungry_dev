# https://www.acmicpc.net/problem/11657

n, m = map(int, input().split())
costs = []

for _ in range(m):
    costs.append(tuple(map(int, input().split())))

def solution(n, m, costs):
    INF = int(10e9)
    shortest = [0 if i <= 1 else INF for i in range(n + 1)]
    
    # 벨만-포드 알고리즘 
    def bellman_ford():
        # n-1번 수행 
        for i in range(n):
            # 모든 간선 탐색 
            for j in range(m):
                start, end, cost = costs[j]
                curr_cost = shortest[start] + cost
                
                # 더 적은 비용을 발견했다면 배열값 갱신 
                if shortest[start] != INF and curr_cost < shortest[end]:
                    shortest[end] = curr_cost
                    
                    # n-1번째에 더 적은 비용이 생겼다는 것은 순환되고 있다는 의미
                    if i == n - 1:
                        return False

        return True
    
    if bellman_ford() is True:
        for cost in shortest[2:]:
            
            # 해당 노드로 가는 간선이 존재하지 않는다면 -1 출력 
            if cost == INF:
                print(-1)
            else:
                print(cost)
    else: # 순환되고 있다면 -1 출력 
        print(-1)

solution(n, m, costs)
