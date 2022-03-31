# https://www.acmicpc.net/problem/1439

S = input()

arr = [0, 0] # 0, 1 개수 저장 배열

# 0번째 숫자 저장
curr = S[0]
arr[int(S[0])] = 1

# 문자 하나씩 확인하며 숫자 바뀔때마다 해당 숫자 개수 1 더하기
for s in S:
    if s != curr:
        arr[int(s)] += 1
        curr = s

# 0, 1 개수 중 가장 작은 개수 출력
print(min(arr))
