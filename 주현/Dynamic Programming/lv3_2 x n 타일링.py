# https://programmers.co.kr/learn/courses/30/lessons/12900

# 1, 2, 3, 5, 8, 13, 21 
# 피보나치 수열 형태로 경우의 수 증가
def solution(n):
    a, b = 1, 1
    
    for _ in range(n - 1):
        # 숫자가 너무 커지면 bigint로 변환되어 연산이 느려짐
        # 다 더하고 나누는것과 나누면서 다 더하는 거는 분배법칙으로 값이 동일
        a, b = b, (a + b) % 1000000007
        
    return b
