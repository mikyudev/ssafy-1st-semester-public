import sys
sys.stdin = open('12712.txt')

T =int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dy1 = [-1, 1, 0, 0]
    dx1 = [0, 0, -1, 1]
    dy2 = [-1, 1, -1, 1]
    dx2 = [1, 1, -1, -1]

    max_v = 0

    for y in range(N):
        for x in range(N):
            sum_v1 = arr[y][x]
            sum_v2 = arr[y][x]
            for i in range(4):
                for j in range(1, M):
                    ny1 = y + dy1[i] * j
                    nx1 = x + dx1[i] * j
                    # if ny1 < 0 or nx1 < 0 or ny1 >=N or nx1 >= N: continue
                    if 0 <= ny1 < N and 0 <= nx1 <N:
                        sum_v1 += arr[ny1][nx1]

                    ny2 = y + dy2[i] * j
                    nx2 = x + dx2[i] * j
                    # if ny2 < 0 or nx2 < 0 or ny2 >=N or nx2 >= N: continue
                    if 0 <= ny2 < N and 0 <= nx2 <N:
                        sum_v2 += arr[ny2][nx2]

                    # sum_v1 += arr[ny1][nx1]
                    # sum_v2 += arr[ny2][nx2]


            if max_v < sum_v1:
                max_v = sum_v1
            if max_v < sum_v2:
                max_v = sum_v2

    print(f"#{tc} {max_v}")




