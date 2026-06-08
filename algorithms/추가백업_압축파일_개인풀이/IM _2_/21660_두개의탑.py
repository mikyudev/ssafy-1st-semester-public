import sys
sys.stdin = open('21660.txt')


T = int(input())

for tc in range(1, T+1):
    N, M1, M2 = map(int, input().split())
    arr = list(map(int,input().split()))

    sum_v = 0

    arr.sort(reverse=True)

    list_1 = list(range(1, M1+1)) + list(range(1, M2+1))
    list_1.sort()

    for i, d in zip(arr, list_1 ):
        sum_v += i * d

    print(f"#{tc} {sum_v}")

