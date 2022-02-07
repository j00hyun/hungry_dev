# https://school.programmers.co.kr/tryouts/32184/challenges

def solution(m, n, infests, vaccinateds):
    answer = -1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_inf = [[inf[0] - 1, inf[1] - 1] for inf in infests]
    
    # 그래프 만들어서 병 걸리거나 백신 맞은 사람 위치 표시
    graph = [[0] * n for _ in range(m)]
    
    for infest in infests:
        graph[infest[0] - 1][infest[1] - 1] = 1
        
    for vaccinated in vaccinateds:
        graph[vaccinated[0] - 1][vaccinated[1] - 1] = 1
        
    # 병에 새로 전염된 직원이 없을 때까지 순회
    while next_inf:
        inf, next_inf = next_inf, []
        answer += 1
        
        # 현재 병에 감염된 직원을 중심으로 주변 직원 감염
        while inf:
            curr = inf.pop()

            for dx, dy in directions:
                x, y = curr[1] + dx, curr[0] + dy

                if 0 <= x < n and 0 <= y < m and graph[y][x] == 0:
                    graph[y][x] = 1
                    next_inf.append([y, x])

    # 모든 전염 끝난 후에 병에 걸리지 않은 직원이 존재한다면 -1
    for y in range(m):
        for x in range(n):
            if graph[y][x] == 0:
                return -1
                    
    return answer
