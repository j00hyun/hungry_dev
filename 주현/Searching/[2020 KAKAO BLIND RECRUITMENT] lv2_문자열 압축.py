# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    
    # 문자열을 자를 단위를 정한다 
    for size in range(1, len(s) // 2 + 1):
        count = 1
        compress = 0
        prev = s[:size]
        
        # 문자열을 압축한다 
        # len(s) + size -> compress를 마지막에 한번 더 시행 (문자열 슬라이싱은 범위를 넘어서도 에러 발생 X)
        for i in range(size, len(s) + size, size):
            curr = s[i:i + size]
            
            if prev == curr:
                count += 1
            else: # 문자열이 서로 다를경우
                compress += len(str(count)) + len(prev) if count > 1 else len(prev)
                prev = curr
                count = 1
                
        # 완전탐색 후 가장 작은 정답값을 찾는다
        answer = min(answer, compress)
        
    return answer
