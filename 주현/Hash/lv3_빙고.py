# https://school.programmers.co.kr/courses/13093/lessons/88769

def solution(board, nums):
    answer = 0
    n = len(board)
    nums = set(nums) # hash
    
    # 숫자 지우기
    for y in range(n):
        for x in range(n): # O(n^2)
            if board[y][x] in nums: # O(n)
                board[y][x] = 0
    
    answer += sum([1 for lst in board if sum(lst) == 0]) # 가로빙고
    answer += sum([1 for lst in zip(*board) if sum(lst) == 0]) # 세로빙고
    answer += int(sum([board[i][i] for i in range(n)]) == 0) # 왼 -> 오 대각선
    answer += int(sum([board[i][n - (i + 1)] for i in range(n)]) == 0) # 오 -> 왼 대각선
    
    return answer
