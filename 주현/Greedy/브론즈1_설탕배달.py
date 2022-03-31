# https://www.acmicpc.net/problem/2839

N = int(input())

# 5kg 봉지를 최대한 많이 들고 갈수 있는 경우부터 계산 
for five in range(N // 5, -1, -1):
    remain = N - five * 5 # 남은 무게 
    
    # 남은 무게가 3kg의 배수로 나누어 떨어진다면 종료 
    # 나누어 떨어지지 않는다면 5kg 봉지 1개 줄이고 다시 계산 
    if remain % 3 == 0:
        print(five + remain // 3)
        break
        
# 어느 경우에도 정확히 Nkg을 맞출 수 없는 경우 -1 리턴 
else:
    print(-1)
