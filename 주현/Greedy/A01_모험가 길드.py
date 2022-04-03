# 이것이 취업을 위한 코딩 테스트다 with 파이썬 311p

from collections import Counter

N = int(input())
counter = Counter(list(map(int, input().split()))) # 공포도에 따른 인원 카운트 
group = 0 # 전체 그룹 수 

for fear, num in counter.items():
    # 최대 그룹 수를 구하는 것이므로, 
    # 해당 공포도 인원으로 새로운 그룹을 몇개 만들 수 있는지 확인하여 그룹 수에 더해줌
    group += num // fear

print(group)
