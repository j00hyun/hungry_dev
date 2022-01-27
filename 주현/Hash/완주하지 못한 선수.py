# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    part_dict = Counter(participant) - Counter(completion)
    return list(part_dict.keys())[0]
