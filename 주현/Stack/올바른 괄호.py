# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    num = 0
    
    for ch in s:
        if ch == '(':
            num += 1
        elif ch == ')':
            num -= 1
            
        if num < 0:
            return False
    
    return num == 0
