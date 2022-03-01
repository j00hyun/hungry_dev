# https://www.acmicpc.net/problem/1806

import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))


# 투포인터 알고리즘
def solution(m, arr):
    left, right = 0, 0
    arr_sum = 0
    min_len = sys.maxsize

    while left <= right:
        if arr_sum >= m:
            min_len = min(min_len, right - left)
            arr_sum -= arr[left]
            left += 1
        else:  # arr_sum < m
            # right가 배열 맨 끝까지 도달했을 경우 종료
            if right == len(arr):
                break

            arr_sum += arr[right]
            right += 1

    # 합이 m 이상인 경우가 존재하지 않는다면 0 리턴
    if min_len == sys.maxsize:
        min_len = 0

    return min_len


print(solution(m, arr))
