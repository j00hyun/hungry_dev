# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    curr = (0, 0)
    direction = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    went_road = set()
    
    for d in dirs:
        x, y = curr[0] + direction[d][0], curr[1] + direction[d][1]
        # (3, 4) -> (3, 5) : (3, 3, 4, 5) 표현 (x, x, y, y)
        road = tuple(sorted([curr[0], x]) + sorted([curr[1], y]))
        
        # 좌표범위를 넘어가면 무시
        if x < -5 or x > 5 or y < -5 or y > 5:
            continue
            
        went_road.add(road)
        curr = x, y
            
    return len(went_road)
