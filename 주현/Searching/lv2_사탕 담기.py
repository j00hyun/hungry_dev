
def solution(m, weights):
    weights.sort(reverse=True)
    
    def recur(weights, total):
        answer = 0
        for idx in range(len(weights)):  
            
            # 가방 남을 경우
            if total + weights[idx] < m:
                if idx + 1 < len(weights):
                    answer += recur(weights[idx+1:], total + weights[idx])
            # 가방 가득 찰 경우 
            elif total + weights[idx] == m:
                answer += 1
                
        return answer
    
    return recur(weights, 0)
