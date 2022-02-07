# https://school.programmers.co.kr/courses/13093/lessons/88759

from heapq import heapify, heappush, heappop
from collections import deque

def solution(healths, items):
    answer = []
    heap = []
    heapify(heap)
    healths.sort()
    
    # 내리는 체력 기준 오름차순 정렬
    items = deque(sorted([[item[1], item[0], i + 1] for i, item in enumerate(items)]))
    
    # 작은 체력 캐릭터부터 순회
    for health in healths:
        while items:
            
            # 아이템 적용 후 체력 100 미만이기 전까지 heap에 저장
            if health - items[0][0] < 100:
                break
            
            debuff, buff, item_num = items.popleft()
            heappush(heap, (-buff, item_num)) # 공격력 기준 최대힙
            
        # 저장된 아이템들 중 가장 큰 공격력 가진 아이템 사용
        # 다음 캐릭터로 이동해도 저장된 아이템은 그대로 유지
        if heap:
            _, num = heappop(heap)
            answer.append(num)
            
    return sorted(answer)
