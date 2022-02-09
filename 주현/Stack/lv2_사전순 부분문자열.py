# https://school.programmers.co.kr/courses/13093/lessons/88772

def solution(s):
    stack = []
    
    for char in s:
        # 이전 알파벳이 현재 알파벳보다 순서가 앞일 경우 삭제
        while len(stack) > 0 and stack[-1] < char:
            stack.pop()
            
        # 이전 알파벳이 현재 알파벳과 순서가 같거나 뒤일 경우 삽입
        stack.append(char)
                
    return ''.join(stack)
