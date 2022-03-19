# https://programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    answer = 0
    length = len(s)
    dp = [[False] * length for _ in range(length)] # 2차원 DP 배열
    
    # 1글자: 무조건 팰린드롬
    for i in range(length):
        dp[i][i] = True
    
    # 2글자: 같은글자가 2개 연속할 경우 팰린드롬
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            
    # 3글자~: 양 끝 글자가 같고 양 끝을 제외한 글자가 팰린드롬이었다면 팰린드롬
    for interval in range(2, length):
        for start in range(length - interval):
            end = start + interval
            
            if s[start] == s[end] and dp[start + 1][end - 1]:
                dp[start][end] = True
    
    # 가장 긴 팰린드롬 길이 찾기
    for start in range(length):
        for end in range(start, length):
            if dp[start][end]:
                answer = max(answer, end - start + 1)
                
    return answer
