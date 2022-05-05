# https://programmers.co.kr/learn/courses/30/lessons/92341

from datetime import datetime
from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    parking = dict() # 입차 된 차 주차 시간 기록
    park_time = defaultdict(int) # 차별 현재 누적 시간 기록
    
    for record in records:
        time, car, state = record.split()
        
        # 입차 기록
        if state == "IN":
            parking[car] = [time, "23:59"]
        
        # 출차 기록
        elif state == "OUT":
            parking[car][1] = time
            
            # 주차 누적 시간 계산
            in_time, out_time = parking.pop(car)
            park_time[car] += (datetime.strptime(out_time, "%H:%M") - datetime.strptime(in_time, "%H:%M")).seconds / 60
            
    # 출차 안한 차량 23:59 출차로 주차 누적 시간 계산
    for car, time in parking.items():
        park_time[car] += (datetime.strptime(time[1], "%H:%M") - datetime.strptime(time[0], "%H:%M")).seconds / 60
    
    # 차번호 오름차 순으로 주차 요금 계산
    for car in sorted(park_time.keys()):
        total_time = park_time[car]
        
        if total_time < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3])
            
    return answer
