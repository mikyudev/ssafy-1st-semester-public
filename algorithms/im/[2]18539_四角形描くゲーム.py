T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]



    max_v = 0
    cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                y1 = y
                x1 = x

                for i in range(y1, N):
                    for j in range(x1, N):
                        if arr[y][x] == arr[i][j]:

                            result = (i-y1+1) * (j-x1+1)

                            if max_v < result:
                                max_v = result
                                cnt = 1

                            elif result == max_v:
                                cnt += 1

    print(f"#{tc} {cnt}")


