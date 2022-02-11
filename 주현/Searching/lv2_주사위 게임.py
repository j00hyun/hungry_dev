# https://school.programmers.co.kr/courses/13093/lessons/88780

from itertools import product
from collections import Counter

def solution(monster, S1, S2, S3):
    total = S1 * S2 * S3
    
    # 주사위 던져서 나올수 있는 모든 경우 sum값 기준으로 딕셔너리 생성
    s_count = Counter(list(map(sum,product(range(1, S1 + 1), range(1, S2 + 1), range(1, S3 + 1)))))
    
    # 몬스터 만나지 않는 경우의 수 
    unmeet_mst = total - sum([s_count[m - 1] for m in monster])
    
    return int((unmeet_mst / total) * 1000)
