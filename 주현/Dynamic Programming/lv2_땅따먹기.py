# https://programmers.co.kr/learn/courses/30/lessons/12913

'''
| 1 | 2 | 3 | 5 |

| 5 | 6 | 7 | 8 |

| 4 | 3 | 2 | 1 |

두번째 행부터 각각 가능한 이전 행의 값들 중 최댓값을 더해 저장한다.

| 1 | 2 | 3 | 5 |

| 10 | 11 | 12 | 11 |

| 16 | 15 | 13 | 13 |
'''
def solution(land):
    # before[i] -> i번째 행을 선택한다고 가정했을 때, 이전 행들 중 선택 가능한 인덱스
    before = [(1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)]
    
    # 두번째 행부터 각각 가능한 이전 행의 값들 중 최댓값을 더해 저장한다.
    for i, arr in enumerate(land):
        
        if i == 0:
            continue
             
        for j in range(4):
            arr[j] += max([land[i - 1][k] for k in before[j]])
                    
    return max(land[-1])
