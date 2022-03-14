# https://programmers.co.kr/learn/courses/30/lessons/72413

def solution(n, s, a, b, fares):
    INF = 100000000
    road = [[0] * (n + 1) if node == 0 else [INF] * (n + 1) for node in range(n + 1)]
    answer = INF
    
    # 자기 자신으로 가는 경우, index 0 비용 0으로 초기화
    for node in range(1, n + 1):
        road[node][node] = 0
        road[node][0] = 0
    
    # 문제에서 주어진 조건으로 배열 초기화
    for c, d, f in fares:
        road[c][d] = f
        road[d][c] = f
    
    # 플루이드워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                road[i][j] = min(road[i][j], road[i][k] + road[k][j])
    
    # k: 합승을 끝내는 지점 -> 모든 경우 고려해 최저 택시요금 계산
    for k in range(1, n + 1):
        answer = min(answer, road[s][k] + road[k][a] + road[k][b])
        
    return answer
