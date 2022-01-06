# https://school.programmers.co.kr/courses/13093/lessons/88778
  
# n 이하 수 중에서 소수 목록 구하기 
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n 

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def solution(n):
    prime_arr = prime_list(n)
    answer = 0
    
    # n이하 소수중에서 3개 수 조합
    for a in range(len(prime_arr)):
        for b in range(a + 1, len(prime_arr)):
            for c in range(b + 1, len(prime_arr)):
                if prime_arr[a] + prime_arr[b] + prime_arr[c] == n:
                    answer += 1
        
    return answer 
