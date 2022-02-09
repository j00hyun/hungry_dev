# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for char in list(s):
        # 동일한 문자가 앞에 있다면 pop
        if stack and stack[-1] == char:
            stack.pop()
        # 앞의 문자랑 다른 문자이면 push
        else:
            stack.append(char)
            
    return int(stack == [])
