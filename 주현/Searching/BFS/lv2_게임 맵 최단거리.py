# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

# BFS
def solution(maps):
    n, m = len(maps[0]), len(maps) # 가로, 세로 길이 
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    maps[0][0] = -1 # 이미 지나온 곳은 -1로 표시
    queue = deque([(0, 0, 1)]) # 현재위치 x, 현재위치 y, 걸어온 칸
    answer = 0
    
    while queue:
        x, y, length = queue.popleft()
        
        # 동서남북 방향으로 이동
        for dx, dy in directions:
            _x, _y = x + dx, y + dy
            
            # 맵 내부에 있고, 갔던 길이 아니고, 벽이 아닌 경우
            if 0 <= _x < n and 0 <= _y < m and maps[_y][_x] == 1:
                
                # 상대팀 진영에 도착한 경우 반환
                if _x == n - 1 and _y == m - 1:
                    return length + 1
                
                # 도착하지 않은 경우, 현재 걸은 길 표시 후 삽입
                maps[_y][_x] = -1
                queue.append((_x, _y, length + 1))
                
    # 상대팀 진영에 절대 갈 수 없는 경우
    return -1
