# https://programmers.co.kr/learn/courses/30/lessons/42895

from itertools import product
from itertools import combinations_with_replacement

def solution(N, number):
    # arrs[N] : 숫자 N이 N개 있을 경우, 표현할 수 있는 모든 수의 집합
    arrs = [{}, {N}]
    
    # N과 number가 같은 경우, 1 리턴
    if N == number:
        return 1
    
    for i in range(2, 9):
        new_set = set()
        # i보다 작은 수 2개를 조합해 i가 되는 경우
        sum_arr = [tuple(c) for c in combinations_with_replacement(range(1, i), 2) if sum(c) == i]
        
        # 해당 인덱스 배열 값들로 가능한 사칙연산 결과를 모두 저장
        for left, right in sum_arr:
            for lst in list(product(arrs[left], arrs[right])):
                # 뺄셈, 나눗셈의 경우 큰거에서 작은거 연산
                a, b = tuple(sorted(lst, reverse=True))
                new_set.update([a + b, a - b, a * b, a // b])
        
        new_set.discard(0) # 0 제거
        new_set.add(int(str(N) * i)) # 숫자를 i개만큼 이어붙인 수 추가
        
        # 결과 set에서 number가 발견되면 종료
        if number in new_set:
            return i
        
        # 다음 계산을 위해 리스트에 저장
        arrs.append(new_set)
        
    return -1
