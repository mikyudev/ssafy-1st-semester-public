
# 비트연산 부분집합 , 부분집합 합

def get_sum(tar):
    sum_v = 0
    for i in range(N):
        if tar & 0x1:
            sum_v += heights[i]
        tar >>= 1
    return sum_v