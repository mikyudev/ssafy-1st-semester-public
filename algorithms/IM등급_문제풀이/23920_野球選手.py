T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    選手 = list(map(int, input().split()))

    選手.sort()


    start = 0
    max_v = 0
    for end in range(N):
        total  = 0
        while 選手[end] - 選手[start] > K:
            start += 1


        total = end - start + 1

        if max_v < total:
            max_v = total

    print(f"#{tc} {max_v}")