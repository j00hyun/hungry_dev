# https://school.programmers.co.kr/courses/13093/lessons/88780

def solution(monster, S1, S2, S3):
    total = S1 * S2 * S3
    meet_mst = 0
    
    for s1 in range(1, S1 + 1):
        for s2 in range(1, S2 + 1):
            for s3 in range(1, S3 + 1):
                # meet monster
                if 1 + s1 + s2 + s3 not in monster:
                    meet_mst += 1
    # 0%
    if meet_mst == 0:
        return 0
    
