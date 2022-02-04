# https://programmers.co.kr/learn/courses/30/lessons/42586

import math
from collections import deque

def solution(progresses, speeds):
    answer = [1]
    queue = deque([math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))])
    std_prg = queue.popleft() # 기준
    
    while len(queue) != 0:
        prg = queue.popleft()
        # 기준보다 작다면 같이 배포
        if std_prg >= prg:
            answer[-1] += 1
        else: # 기준보다 크면 다른날 배포
            answer.append(1)
            std_prg = prg
    
    return answer
