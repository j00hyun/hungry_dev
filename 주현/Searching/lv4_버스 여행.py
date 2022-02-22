# https://school.programmers.co.kr/courses/13093/lessons/88783

from collections import deque

def solution(n, signs): 
    
    # 첫째 줄부터 탐색
    for start in range(n):
        queue = deque([i for i, sign in enumerate(signs[start]) if sign == 1])

        while queue:
            end = queue.popleft()
            
            # 환승하여 새로운 목적지를 갈 수 있다면 표시 후 큐에 추가
            for i, sign in enumerate(signs[end]):
                if sign == 1 and signs[start][i] == 0:
                    signs[start][i] = 1
                    queue.append(i)
                    
    return signs
