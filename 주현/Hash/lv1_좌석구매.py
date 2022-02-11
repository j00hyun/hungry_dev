# https://school.programmers.co.kr/tryouts/32187/challenges

def solution(seat):
    # hash 내부에는 list가 들어갈 수 없음
    return len(set([tuple(s) for s in seat])) # len(set(list(map(tuple, seat))))
