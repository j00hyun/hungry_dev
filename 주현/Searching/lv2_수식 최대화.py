# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations

def solution(expression):
    exp_arr, oper_set = [], set() # 입력값 연산자 기준으로 나눈 배열, 연산자 set
    num = ''
    answer = 0
    
    # 입력값 연산자 앞뒤 기준으로 나누어서 배열 생성
    for e in expression:
        if not e.isdigit():
            exp_arr += [num, e]
            oper_set.add(e)
            num = ''
        else:
            num += e
            
    exp_arr.append(num)
    
    # 연산자 우선순위 순열만큼 반복
    for seq in permutations(oper_set, len(oper_set)):
        _exp_arr = exp_arr[:]
        
        for operator in seq:
            while operator in _exp_arr:
                for i, value in enumerate(_exp_arr):
                    
                    # 현재 찾는 연산자가 존재하는 배열 위치에서 연산자, 앞, 뒤 숫자를 추출해 연산을 해서 다시 배열에 저장
                    if value == operator:
                        _exp_arr[i - 1] = str(eval(_exp_arr[i - 1] + value + _exp_arr[i + 1]))
                        _exp_arr = _exp_arr[:i] + _exp_arr[i + 2:]
                        break
        
        # 절대값 중 가장 큰 값 저장 
        answer = max(answer, abs(int(_exp_arr[0])))
        
    return answer
