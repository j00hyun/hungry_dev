# https://programmers.co.kr/learn/courses/30/lessons/17685

# trie 생성
def make_trie(words):
    root = {}
    
    for word in words:
        curr = root
        
        for letter in word:
            curr.setdefault(letter, [0, {}]) # 단어 수 계산
            curr[letter][0] += 1
            curr = curr[letter][1]
            
    return root

def solution(words):
    answer = 0
    trie = make_trie(words)
    
    for word in words:
        curr = trie
        
        for i, letter in enumerate(word):
            # 해당 문자에 포함되는 단어가 1개만 존재할 경우
            if curr[letter][0] == 1:
                answer += i + 1
                break
            curr = curr[letter][1]
        # 중복되는 단어가 존재해서 단어를 끝까지 탐색 했을 경우
        else:
            answer += i + 1
                
    return answer
