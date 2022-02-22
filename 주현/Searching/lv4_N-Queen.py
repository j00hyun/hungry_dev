# https://programmers.co.kr/learn/courses/30/lessons/12952

# 세로, 대각선 방향으로 다른 퀸이 존재하는지 확인
def check(queen, y):
    for i in range(y):
        if queen[i] == queen[y] or y - i == abs(queen[y] - queen[i]):
            return False
    
    return True

# 가능한 방법의 수 리턴
def search(queen, y):
    count = 0
    n = len(queen)
    
    # y가 배열 범위를 초과하면 이미 배치가 끝난 것이므로 1 리턴
    if y == n:
        return 1
    
    # 퀸을 일단 배치한 후 check 함수로 배치할 수 있는 경우인지 확인
    for x in range(n):
        queen[y] = x
        
        if check(queen, y) is True:   
            count += search(queen, y + 1)
            
    return count
    
# 가로에 퀸을 1개만 놓을 수 있으므로 1차원 배열로 표현
# 행 : index, 열 : queen[index]
def solution(n):
    return search([0] * n, 0)
