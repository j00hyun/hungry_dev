# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    map_arr = [[0] * (m + 1) for _ in range(n + 1)]
    map_arr[1][1] = 1 # 집
    
    # 물이 잠긴 곳 -1 로 표시
    for x, y in puddles:
        map_arr[y][x] = -1
        
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            
            # 물이 잠긴 곳일 경우 다음 계산을 위해 0으로 초기화 후 넘어감
            if map_arr[y][x] == -1:
                map_arr[y][x] = 0
                continue
            
            # 왼쪽, 위쪽 값 더해 현재 값 세팅 (미리 나누어줌)
            map_arr[y][x] += (map_arr[y - 1][x] + map_arr[y][x - 1]) % 1000000007
            
    return map_arr[n][m]
