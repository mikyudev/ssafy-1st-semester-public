T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]



    max_v = 0
    for y in range(N):
        for x in range(N):
            total = arr[y][x]
            for i in range(4):
                for j in range(1, K+1):
                    ny = y + dy[i] * j
                    nx = x + dx[i] * j

                    if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
                    total += arr[ny][nx]


            if max_v < total:
                max_v = total

    print(f"#{tc} {max_v}")
