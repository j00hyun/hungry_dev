# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    arr = [] # 문제 행렬
    answer = []
    
    # 문제 행렬 생성 
    for y in range(rows):
        arr.append([x for x in range(y * columns + 1, (y + 1) * columns + 1)])
    
    # 행렬 회전하면서 가장 작은 숫자 추출
    for y1, x1, y2, x2 in queries:
        _arr = [item[:] for item in arr] # 현재 행렬 상태 복사
        x, y = x1 - 1, y1 - 1 # 행렬에서 현재 위치 
        min_num = 100000 # 가장 작은 숫자 저장
        
        for x in range(x1, x2):
            arr[y][x] = _arr[y][x - 1]
            min_num = min(min_num, arr[y][x])

        for y in range(y1, y2):
            arr[y][x] = _arr[y - 1][x]
            min_num = min(min_num, arr[y][x])
        
        for x in range(x2 - 2, x1 - 2, -1):
            arr[y][x] = _arr[y][x + 1]
            min_num = min(min_num, arr[y][x])
        
        for y in range(y2 - 2, y1 - 2, -1):
            arr[y][x] = _arr[y + 1][x]
            min_num = min(min_num, arr[y][x])

        answer.append(min_num)    
        
    return answer
