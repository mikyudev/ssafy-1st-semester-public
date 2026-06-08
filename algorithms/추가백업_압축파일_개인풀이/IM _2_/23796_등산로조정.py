import sys
sys.stdin = open('23796.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]


    max_v = 0
    for y in range(N):
        for x in range(N):
            current_y, current_x = y, x
            min_h = float('inf')               ######### @@@@@@@@@@@@
            cnt = 1                           ######  @@@@@@@
            while True:          #!!#!!##!!
                # min_h = float('inf')
                next_y = -1
                next_x = -1
                for i in range(4):
                    ny = current_y + dy[i]
                    nx = current_x + dx[i]
                    if ny <0 or nx < 0 or ny >= N or nx >= N or arr[ny][nx] >= arr[current_y][current_x]: continue

                    if min_h > arr[ny][nx]:
                        min_h = arr[ny][nx]
                        next_y = ny
                        next_x = nx

                if next_y != -1:
                    current_y, current_x = next_y, next_x         #### @@@@@@
                    cnt +=1
                else:
                    break
            if max_v < cnt:
                max_v = cnt

    print(f"#{tc} {max_v}")

