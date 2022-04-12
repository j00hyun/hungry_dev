# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import defaultdict

def solution(str1, str2):
    strs = [str1, str2] # 입력 배열화
    union, inter = 0, 0 # 합집합, 교집합
    dicts = [defaultdict(int), defaultdict(int)] # 단어별 갯수 
    word_set = set() # str1, str2 단어 모음
    
    # 각 단어 count해서 dicts에 저장
    for i, string in enumerate(strs):
        for j in range(len(string) - 1):
            word = string[j:j + 2]
            
            # 알파벳으로 이루어져 있을 경우만 소문자로 변환해 저장 
            if word.isalpha():
                dicts[i][word.lower()] += 1
                word_set.add(word.lower())
    
    # 교집합, 합집합 수 계산 
    for word in word_set:
        words = dicts[0][word], dicts[1][word]
        union += min(words) # 둘 중 1개에만 존재할경우 0
        inter += max(words)
        
    # 합집합이 0인 경우 자카드 유사도 1
    return 65536 if inter == 0 else int(union / inter * 65536)
