# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

def solution(places):
    answer = []
    side = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 옆 자리 
    two_side = [(-2, 0), (2, 0), (0, -2), (0, 2)] # 옆옆 자리  
    cross = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 대각선 자리
    
    # 해당 응시자가 거리두기 지키고 있는지 확인
    def is_correct(x, y):
        
        # 응시자 옆자리 체크
        for dx, dy in side:
            _x, _y = x + dx, y + dy
            # 응시자 옆자리에 다른 사람 있으면 거리두기 위반
            if 0 <= _x <= 5 and 0 <= _y <= 5 and (_x, _y) in person:
                return False
        
        # 응시자 옆옆자리 체크
        for dx, dy in two_side:
            _x, _y = x + dx, y + dy
            p = ((x + _x) / 2, (y + _y) / 2) # 응시자 - 옆옆자리 사이 파티션 위치
            # 사이에 파티션 없이 응시자 옆옆자리에 사람이 있으면 거리두기 위반
            if 0 <= _x <= 5 and 0 <= _y <= 5 and (_x, _y) in person and p not in partition:
                return False
        
        # 응시자 대각선 자리 체크
        for dx, dy in cross:
            _x, _y = x + dx, y + dy
            p1, p2 = (x, _y), (_x, y) # 응시자 - 대각선 사이 파티션 위치
            # 양 대각선 파티션 1개라도 없이 대각선에 다른 사람 앉아있으면 거리두기 위반
            if 0 <= _x <= 5 and 0 <= _y <= 5 and (_x, _y) in person and (p1 not in partition or p2 not in partition):
                return False
        
        return True
    
    # 본격 로직 시작
    for place in places:
        person, partition = set(), set() # 응시자 위치, 파티션 위치
        
        # 응시자, 파티션 위치 저장
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    person.add((x, y))
                elif place[y][x] == 'X':
                    partition.add((x, y))
        
        # 각 응시자마다 거리두기 확인
        for x, y in person:
            # 1명이라도 거리두기 지키지 않으면 0 
            if not is_correct(x, y):
                answer.append(0)
                break
        else: # 모두 거리두기 지켰을 경우 1
            answer.append(1)
            
    return answer
