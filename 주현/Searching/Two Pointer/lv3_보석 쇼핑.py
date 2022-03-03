# https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict

def solution(gems):
    left, right = 0, 0
    gem_dict = defaultdict(int)
    gem_num = len(set(gems))
    answer = [1, len(gems)]
    
    while left <= right:
        # 맨 왼쪽 보석과 같은 보석이 나머지 보석 중에 존재할 경우 left++
        if gem_dict[gems[left]] > 1:
            gem_dict[gems[left]] -= 1
            left += 1
        # 오른쪽으로 더 보석이 존재할 경우 right++
        elif right < len(gems):
            gem_dict[gems[right]] += 1
            right += 1
        # 오른쪽으로 더이상 보석이 존재하지 않을 경우 종료
        else:
            break
        
        # 모든 보석이 존재하고 현재 답보다 길이가 짧을 경우 답 변경
        if len(gem_dict.keys()) == gem_num and right - left <= answer[1] - answer[0]:
            answer = [left + 1, right]
        
    return answer
