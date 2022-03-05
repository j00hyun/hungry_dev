# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer = 0
    
    for n in d:
        # 예산 초과할 경우 종료
        if budget - n < 0:
            break
        
        budget -= n
        answer += 1
        
    return answer
