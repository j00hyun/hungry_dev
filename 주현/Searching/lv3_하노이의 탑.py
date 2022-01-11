# https://school.programmers.co.kr/tryouts/32189/challenges?language=python3

def solution(n):
    answer = []
    
    def hanoi(n, st, fn, to):
        # 원반이 한개라면 종료 
        if n == 1:
            answer.append([st, fn])
            return
        
        # 원반 n-1개를 to로 이동 (fn가 보조기둥)
        hanoi(n-1, st, to, fn)
        # 가장 큰 원반 fn로 이동
        answer.append([st, fn])
        # to에 있는 n-1개 원반을 fn으로 이동
        hanoi(n-1, to, fn, st)
    
    hanoi(n, 1, 3, 2)
    return answer
