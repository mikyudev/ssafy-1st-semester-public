T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    正解 = list(map(int, input().split()))

    生徒 = [list(map(int, input().split())) for _ in range(N)]

    min_v = float('inf')
    max_v = float('-inf')


    for y in range(N):
        cnt = 0
        total = 0
        for x in range(M):
            if 生徒[y][x] ==  正解[x]:
                total += cnt +1
                cnt += 1

            if 生徒[y][x] !=  正解[x]:
                cnt = 0



        if max_v < total:
            max_v = total

        if min_v > total:
            min_v = total


    print(f"#{tc} {max_v - min_v}")






