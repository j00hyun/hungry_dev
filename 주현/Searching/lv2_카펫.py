# https://school.programmers.co.kr/courses/13093/lessons/88781

# brown : x+y = (b-8)/2 + 6
# red: (x-2) * (y-2) = r
# x >= y, x,y >= 3
def solution(brown, red):
    answer = [0, 0]
    
    # 3 X 3
    if brown == 8:
        return [3, 3]
    
    # (w+h-6) * 2 = brown-8
    tot_len = (brown - 8) // 2 +6
    # w >= h >= 3
    for w in range(tot_len // 2 + tot_len % 2, tot_len - 2):
        h = tot_len - w
        
        if (w - 2) * (h - 2) == red:
            answer = [w, h]
            break
            
    return answer
