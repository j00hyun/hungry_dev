# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time, w = 0, 0 # 경과 시간, 다리에 있는 트럭 총 무게
    trucks, bridge = deque(truck_weights), deque() # 대기 트럭, 다리를 건너는 트럭
    
    # 다리를 건너는 트럭과 대기 트럭이 모두 없을 때까지 실행
    while trucks or bridge:
        time += 1
        
        # 다리를 빠져나갈 트럭이 존재하면 다리에서 제거
        if bridge and bridge[0][1] == time:
            w -= bridge.popleft()[0]
            
        # 대기 트럭 존재하고 다리의 트럭 최대 수, 무게를 만족하면 다리에 대기 트럭 1개 삽입
        if trucks and len(bridge) < bridge_length and w + trucks[0] <= weight:
            w += trucks[0]
            bridge.append((trucks.popleft(), time + bridge_length)) # (트럭의 무게, 다리를 빠져나갈 시간)
            
    return time
