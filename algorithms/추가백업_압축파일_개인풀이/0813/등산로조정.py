T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dy = [ -1, 1, 0, 0]
    dx = [ 0, 0, -1, 1]

    max_v = 0
    for y in range(N):
        for x in range(N):
            current_y, current_x = y, x
            cnt = 1 # 시작점 포함 안 했다 .;

            while True:   # 이 부분 중요 !
                next_y, next_x = -1, -1
                min_h = float('inf')

                for i in range(4):
                    ny = current_y +dy[i]
                    nx = current_x +dx[i]
                    if ny <0 or nx <0 or ny >= N or nx >= N or arr[ny][nx] >= arr[current_y][current_x]: continue
                    # 여기까지 왔으면 조건 통과 한 애들

                    if min_h > arr[ny][nx]:
                        min_h = arr[ny][nx]
                        next_y = ny # 이거 틀림
                        next_x = nx  # 이거 틀림

                if next_y != -1: # 이거 틀림
                    current_y, current_x = next_y, next_x # 이거 틀림
                    cnt += 1  # 이거 틀림

                else:       # 이거 틀림
                    break   # 이거 틀림



            if max_v < cnt:
                max_v =cnt



    print(f"#{tc} {max_v}")




                # 가장 낮은 곳으로 이동




