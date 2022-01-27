# https://programmers.co.kr/learn/courses/30/lessons/49993

from collections import deque

def solution(skill, skill_trees):
    result = 0
    
    for skill_tree in skill_trees:
        skill_deque = deque(skill)
        
        for s in skill_tree:
            if s in skill and s != skill_deque.popleft():
                break
        else: # skill_tree 끝까지 탐색한 경우
            result += 1
            
    return result
