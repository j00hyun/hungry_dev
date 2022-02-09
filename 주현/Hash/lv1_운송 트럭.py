# https://school.programmers.co.kr/courses/13093/lessons/88768

def solution(max_weight, specs, names):
    answer = 1
    truck_weight = 0
    specs_dict = dict(specs)
    # specs_dict = {name: weight for name, weight in specs}
    
    for name in names:
        weight = int(specs_dict[name])
        
        # 트럭 허용 무게 보다 커질 경우
        if truck_weight + weight > max_weight:
            answer += 1
            truck_weight = weight
        else:
            truck_weight += weight
    
    return answer
