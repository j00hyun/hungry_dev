# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    print_num = 1 # 인쇄 완료 개수
    priorities = deque([(i, p) for i, p in enumerate(priorities)]) # (대기순서, 중요도)
    curr_wait, curr_priority = priorities.popleft()
    
    while priorities:
        
        # 중요도가 더 큰게 존재한다면 맨 뒤로 문서 보내기
        for _, priority in priorities:
            if priority > curr_priority:
                priorities.append((curr_wait, curr_priority))
                break
                
        # 중요도가 더 큰 문서가 존재하지 않는다면
        else:
            # 현재 인쇄 문서 대기번호가 내가 요청한 문서일 경우 인쇄 완료 갯수 리턴
            if curr_wait == location:
                break
            # 인쇄 완료 갯수 1 증가
            print_num += 1
        
        # 다음 문서 대기목록에서 꺼냄
        curr_wait, curr_priority = priorities.popleft()
    
    return print_num
