# https://programmers.co.kr/learn/courses/30/lessons/43162#

# union-find
def solution(n, computers):
    networks = [i for i in range(n)]
    root = set()
    
    # find
    def find(i):
        if networks[i] == i:
            return i
        else:
            networks[i] = find(networks[i])
            return networks[i]
        
    # 행렬 대각선 기준으로 대칭이므로 왼쪽 부분만 검색
    for y in range(n):
        for x in range(y):
            if computers[y][x] == 1:
                # union
                x_root, y_root = find(x), find(y)
                networks[y_root] = x_root
    
    # 네트워크 root개수 계산
    for computer in networks:
        root.add(find(computer))
        
    return len(root)
