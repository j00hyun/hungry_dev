# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    name = dict() # 아이디별 최종 닉네임
    answer = []
    
    # 아이디별 최종 닉네임 name 딕셔너리에 담음
    for log in record:
        cmd = log.split()[0]
        if cmd == "Enter" or cmd == "Change":
            _, user, nickname = log.split()
            name[user] = nickname
    
    # 채팅방 들어오거나 나간 기록 최종 닉네임으로 로그 생성
    for log in record:
        cmd, user = log.split()[0], log.split()[1]
        if cmd == "Enter":
            answer.append(name[user] + "님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(name[user] + "님이 나갔습니다.")
            
    return answer
