# https://www.acmicpc.net/problem/3055

from collections import deque

n, m = map(int, input().split())
arr = []
queue = deque()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 'KAKTUS'

for y in range(n):
    _arr = list(input())
    arr.append(_arr)

    # 고슴도치 시작 지점 큐에 추가
    if 'S' in _arr:
        queue.append((0, y, _arr.index('S')))

# 물이 있는 지점 큐에 추가
for y in range(n):
    for x in range(m):
        if arr[y][x] == '*':
            queue.append(('*', y, x))


while queue:
    check, y, x = queue.popleft()

    # 고슴도치가 물에 침수된 경우 다음 큐로 이동
    if check != '*' and arr[y][x] == '*':
        continue

    # 물과 고슴도치가 상하죄우 중 갈 수 있는 지점 체크
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:

            # 물 퍼트리기
            if check == '*':
                if arr[ny][nx] != '*' and arr[ny][nx] != 'X' and arr[ny][nx] != 'D':
                    arr[ny][nx] = '*'
                    queue.append(('*', ny, nx))

            # 고슴도치
            else:
                # 고슴도치 지난 곳 표시 (고슴도치가 갔던 곳은 다시 방문할 필요 X)
                if arr[ny][nx] == '.':
                    arr[ny][nx] = '_'
                    queue.append((check + 1, ny, nx))

                # 고슴도치가 굴에 도착했을 경우 종료 후 이동거리 출력
                if arr[ny][nx] == 'D':
                    answer = check + 1
                    break

    if answer != 'KAKTUS':
        break

# 고슴도치가 더이상 굴쪽으로 이동할 수 없을 경우 'KAKTUS' 출력
print(answer)
