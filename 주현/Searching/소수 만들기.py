# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    answer = 0
    sums = [sum(c) for c in combinations(nums, 3)]
    
    for s in sums:
        # 1, 자기자신 이외의 것으로 나눴는데 나누어떨어지면 소수가 아님
        for n in range(2, s):
            
            if s % n == 0:
                break   
                
        else:
            answer += 1
                
    return answer
