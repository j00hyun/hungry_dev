# https://school.programmers.co.kr/courses/13093/lessons/88756

from collections import deque

def solution(n, m, image):
    answer = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    for sy in range(n):
        for sx in range(m):
            if image[sy][sx] == 0:
                continue

            target_color = image[sy][sx]
            queue = deque([(sy, sx)])
            
            # BFS 핵심 로직
            while queue:
                y, x = queue.popleft()
                
                # 갈수 있는 곳 탐색
                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= nx < m and 0 <= ny < n and image[ny][nx] == target_color:
                        image[ny][nx] = 0
                        # 갈수 있다면 큐에 추가
                        queue.append((ny, nx))

            answer += 1
    
    return answer
