# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

# BFS (최단거리)
def solution(begin, target, words):
    queue = deque([[begin]])
    
    while queue:
        progress = queue.popleft()
        curr = progress[-1]
        
        # 현재 단어가 target과 같다면 종료
        if curr == target:
            return len(progress) - 1
        
        # 현재까지 사용한 단어가 아니고, 알파벳 1개만 차이가 날 경우 큐에 저장
        for word in words:
            if word not in progress and sum(b != w for b, w in zip(curr, word)) == 1:
                queue.append(progress + [word])
    
    # target 단어로 변환이 불가능한 경우 
    return 0
