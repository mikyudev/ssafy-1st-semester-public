import sys
sys.stdin = open("정사각.txt")






dy = [-1, 1 ,0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1) # 1번 ~ N^2 번 방 번호  +1 은 1번 부터 시작이라서

    # 현재 위치 숫자 기준 상하좌우를 확인
    # -> 1 큰 게 있으면 visited에 1이라고 체크
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y +dy[i]
                nx = x +dx[i]

                if ny < 0 or nx < 0 or ny >= N or nx >= N: continue


                if arr [ny][nx] == arr[y][x] + 1:
                    visited[arr[y][x]] = 1
                    break

    # print(visited)

    max_cnt = 0 # 정답
    cnt = 0 # 하나하나 마다 몇 개가 연속되는지
    start = 0 # 숫자를 세기 시작한 위치
    for i in range(1, N*N +1):
        if visited[i] ==1:
            cnt +=1
        else:
            if max_cnt < cnt:
                max_cnt = cnt # 최대값 갱신
                start = i - cnt  # 시작점 찾기
            cnt = 0

    print(f"#{tc} {start} {max_cnt + 1 } ")



