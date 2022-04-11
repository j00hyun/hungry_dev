# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for c in course:
        order_dict = defaultdict(int) # 메뉴 구성 당 주문 수
        
        # 메뉴 구성 당 주문 수 저장
        for order in orders:
            for com in combinations(order, c):
                order_dict[''.join(sorted(com))] += 1
        
        # 주문 수 2 이상이어야 함
        if order_dict and max(order_dict.values()) > 1:
            max_order = max(order_dict.values())
            
            # 주문 수가 가장 많은 메뉴 구성 answer 배열에 저장
            for key, value in order_dict.items():
                if value == max_order:
                    answer.append(key)
                    
    return sorted(answer)
