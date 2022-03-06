# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    # ex) '3' < '30' 이어야 하므로
    # 1000 이하인 것 참고해 '333' < '303030' 으로 판단
    numbers.sort(key=lambda n: str(n) * 3, reverse=True)
    return str(int(''.join(str(n) for n in numbers)))
