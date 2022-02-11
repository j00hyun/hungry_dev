# https://school.programmers.co.kr/tryouts/32188/challenges

def solution(s):
    stack = []
    cursors = {')': '(', 
               '}': '{', 
               ']': '['}
    
    for c in s:
        
        # 닫는 괄호
        if c in cursors.keys():
            
            # 짝이 맞을 경우
            if stack and stack[-1] == cursors[c]:
                stack.pop()
            else:
                return False
            
        # 여는 괄호
        else:
            stack.append(c)
    
    return stack == []
