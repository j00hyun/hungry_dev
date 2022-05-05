# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    set_nums = set(nums) # 폰켓몬 종류 수
    
    # 폰켓몬 종류 수가 골라야하는 수보다 많을 경우
    if len(set_nums) > len(nums) // 2:
        return len(nums) // 2
    # 폰켓몬 종류 수가 골라야하는 수보다 적을 경우
    else:
        return len(set_nums)
