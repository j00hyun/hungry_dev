# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserve.sort()
    lost = set(lost)
    
    # 여분을 가져왔는데 잃어버린 학생 0으로 처리
    for i, r in enumerate(reserve):
        if r in lost:
            lost.remove(r)
            reserve[i] = 0
    
    for r in reserve:
        # 여분을 가져왔는데 잃어버린 학생인지 체크
        if r == 0: 
            continue
            
        # 앞, 뒤 빌려주기
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
            
    return n - len(lost)
