# 이것이 취업을 위한 코딩 테스트다 with 파이썬 312p

nums = input()
curr = 0

for n in nums:
    n = int(n)

    # 둘 숫자 중에 하나라도 0 또는 1일 경우에만 *보다 +가 값이 더 커진다.
    if curr in {0, 1} or n in {0, 1}:
        curr += n
    else:
        curr *= n

print(curr)
