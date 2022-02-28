# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())))


def solution(m, trees):
    # 이진 탐색
    min_height, max_height = 0, trees[-1]
    mid_height = (min_height + max_height) // 2

    # min_height와 max_height 사이에 새로운 값이 없을 때 까지 진행
    while mid_height != min_height:
        # 절단 후 나무 높이 합 계산
        tree_len = sum(tree - mid_height for tree in trees if tree > mid_height)

        # m미터에 딱 맞아떨어질 경우 해당 값 출력
        if tree_len == m:
            return mid_height
        elif tree_len > m:
            min_height = mid_height
        else:  # tree_len < m
            max_height = mid_height

        # 중간값 새로 계산
        mid_height = (min_height + max_height) // 2

    # m미터 이상 나무를 가져갈 수 있는 최대 높이값 출력
    return min_height


print(solution(m, trees))
