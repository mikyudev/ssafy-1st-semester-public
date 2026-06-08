T = int(input())
for tc in range(1, T+1):
    N, K  = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    total = 0
    for y in range(N):
        cnt = 0
        for x in range(N):
            if arr[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0

        if cnt == K:
            total += 1


    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt == K:
            total += 1

    print(f"#{tc} {total}")