T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N+1)]

    max_v = 0
    for y in range(N+1):
        for x in range(N+1):
            if arr[y][x] == 2:
                y2 = y
                x2 = x
                for i in range(N+1):
                    for j in range(N+1):
                        if arr[i][j] == 1:

                            d = (y2 - i)**2 + (x2 - j)**2

                            if max_v < d:
                                max_v = d

    radius = 0
    while radius * radius < max_v:
        radius += 1

    print(f"#{tc} {radius} ")


