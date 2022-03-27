# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    words_set = set()
    
    for i, word in enumerate(words):
        words_set.add(word)
        
        # 단어가 중복되거나, 앞단어의 끝과 현재단어의 시작 알파벳이 다를 경우
        if len(words_set) == i or (i > 0 and words[i - 1][-1] != word[0]):
            # [번호, 차례] 리턴
            return [i % n + 1, i // n + 1]
    
    # 탈락자가 없을 경우
    return [0, 0]
