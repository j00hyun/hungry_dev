# https://programmers.co.kr/learn/courses/30/lessons/43238#

def solution(n, times):
    min_time, max_time = min(times), min(times) * n
    
    # 이진탐색 바로 인접한 값으로 도달할때 까지 진행
    while min_time < max_time:
        mid_time = (min_time + max_time) // 2
        
        # mid_time동안 심사할 수 있는 인원 수
        done_person = sum(mid_time // time for time in times)
        
        # 심사완료 인원이 n보다 크거나 같을경우
        if done_person >= n:
            max_time = mid_time
        # 심사완료 인원이 n보다 작을 경우
        else:
            min_time = mid_time + 1
    
    # 심사완료 인원이 n이상이 되는 최솟값
    return min_time
