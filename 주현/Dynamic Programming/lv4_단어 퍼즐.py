# https://programmers.co.kr/learn/courses/30/lessons/12983

# DP
def solution(strs, t):
    strs = set(strs)
    arr = [0 if i == 0 else 30000 for i in range(len(t) + 1)]
    
    # b -> 0
    # ba -> b a(0), ba(1) -> 1
    # ban -> ba n(2), b an(0), ban(0) -> 2
    # bana -> ban n(3), ba na(2), b ana(0), bana(0) -> 2
    # banan -> bana n(3), ban an(0), ba nan(0), b anan(0), banan(0) -> 3
    # banana -> banan a(4), bana na(3), ban ana(0), ba nana(0), b anana(0), banana(0) -> 3
    # arr = [0, 0, 1, 2, 2, 3, 3]
    
    for curr in range(1, len(t) + 1):
        for l in range(1, min(curr + 1, 6)):
            
            left = t[:curr - l]
            right = t[curr - l:curr]
            
            # 뒷부분 문자열이 strs 배열 내에 존재한다면
            if right in strs:
                # 현재 최솟값과 앞부분 문자열 + 1 중 더 작은 것을 저장
                arr[curr] = min(arr[curr], arr[curr - l] + 1)
    
    # 해당 단어를 만들 수 있다면 최솟값 반환
    return -1 if arr[-1] == 30000 else arr[-1]
