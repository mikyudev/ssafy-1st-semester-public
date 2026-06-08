T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    total = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 0:
                total+= 1



    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                cnt = 0
                for i in range(4):
                    for j in range(1, N):
                        ny = y + dy[i] * j
                        nx = x + dx[i] * j
                        if ny <0 or nx <0 or ny >= N or nx >= N: continue

                        if arr[ny][nx] == 1:
                            break
                        if arr[ny][nx] == 0:
                            cnt += 1


    print(f"#{tc} {total-cnt}")


