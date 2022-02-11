# https://programmers.co.kr/learn/courses/30/lessons/60059

# 자물쇠 확장하기
def expand_lock(key, lock, M, N):
    length = M * 2 + N
    expanded_lock = [[0] * length for _ in range(length)]
    
    for y in range(N):
        for x in range(N):
            expanded_lock[M + y][M + x] = lock[y][x]
    
    return expanded_lock

# 열쇠 회전하기
def turn_key(key):
    return [list(reversed(item)) for item in zip(*key)] # list[::-1]

# 열쇠-자물쇠 합치기
def unlock(key, expanded_lock, x, y, M, N):
    _lock = [item[:] for item in expanded_lock]
    
    # 열쇠와 자물쇠 합치기
    for k_y in range(M):
        for k_x in range(M):
            _lock[y + k_y][x + k_x] += key[k_y][k_x]      
                    
    # 자물쇠에 빈 부분이 없는지 체크
    for l_y in range(N):
        for l_x in range(N):
            if _lock[M + l_y][M + l_x] != 1:
                return False
                
    return True
    
def solution(key, lock):
    M, N = len(key), len(lock)
    
    # 자물쇠 확장하기
    expanded_lock = expand_lock(key, lock, M, N)
    
    # 열쇠 90도 씩 회전하기
    for _ in range(4):
        key = turn_key(key)
        
        # 열쇠 움직이며 확인
        for l_y in range(len(expanded_lock) - M):
            for l_x in range(len(expanded_lock) - M):
                if unlock(key, expanded_lock, l_x, l_y, M, N) is True:
                    return True
                
    return False
