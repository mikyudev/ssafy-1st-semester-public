# 벽돌 깨기
# 1. 최소 벽돌
#  - 현재 벽돌이 다 깨지면 더 이상 할 필요가 없다 -> 현재 벽돌 수를 관리


# N 번의 구슬을 굴려야 한다.
# - 모든 케이스를 보아야 한다. (12 ^ 4, 약 25만 번)
# - 백트래킹
    # - 한 번 쏘았을 때 벽돌들이 연쇄로 꺠진다.
    # - 현재 기준으로 퍼져나가면서 탐색 (BFS)
    # - 빈칸 메우기 (


from _collections import deque


# 핵심 로직
def shoot(cnt, remains, now_arr):
    global  min_blocks
    # 종료 조건 : N 개의 구슬을 모두 발사 or 남은 벽돌이 0이면
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return


    # 모든 열에 한 줄씩 떨구자
    for col in range(W):
        # 방법 1. 원본을 복사해두고, 다시 되돌리는 방법
        # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복사 주의)
        # 2. 원본 리스트의 col 위치에 떨구고
        # 3. cnt + 1 번 재귀상태로 이동
        # 4. 떨구기 전 상태로 복구

    # 방법 2. 복구시간이 없는 방식
        # 1. col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 떨군다.
        # 3. cnt + 1 번 상태로 이동할 때, copy_arr

        copy_arr = [row[:]for row in now_arr]


        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if arr[now_r][col]:
                row = r
                break


        if row == -1: # 벽돌이 없는 열은 pass
            continue

        # 해당 row, col 의 숫자부터 시작해서 BFS
        # 행, 열, 숫자를 모두 담아야 한다.
        q = deque([row, col, arr[row][col]])
        now_remains = remains -1

        arr[row][col] = 0 # 구슬이 처음 만나는 벽돌 자리

        # 주변 벽돌들을 순차적으로 파괴
        # 빈칸을 메우기

        shoot(cnt + 1, now_remains)





T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    min_blocks = 1e9 # 최소 벽돌 수
    blocks = 0
    # 남은 벽돌 수

    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    shoot() # 남은 거 가지고 구슬을 쏠거래
    print(f"#{tc} {min_blocks}")






































    from collections import deque


    def boom(y, x, arr):
        q = deque()
        p = arr[y][x]
        arr[y][x] = 0
        if p > 1:
            q.append((y, x, p))
        while q:
            cy, cx, power = q.popleft()
            for d in range(4):
                ny, nx = cy, cx
                for _ in range(power - 1):
                    ny += dy[d];
                    nx += dx[d]
                    if ny < 0 or nx < 0 or ny >= H or nx >= W: break
                    if arr[ny][nx] == 0: continue
                    np = arr[ny][nx]
                    arr[ny][nx] = 0
                    if np > 1: q.append((ny, nx, np))


    def drop(arr):
        for x in range(W):
            b = H - 1
            for y in range(H - 1, -1, -1):
                if arr[y][x]:
                    arr[b][x] = arr[y][x]
                    if b != y: arr[y][x] = 0
                    b -= 1
            for y in range(b, -1, -1): arr[y][x] = 0


    def dfs(lev, arr):
        global mx
        if lev == N:
            mx = max(mx, sum(r.count(0) for r in arr))
            return
        for x in range(W):
            y = 0
            while y < H and arr[y][x] == 0: y += 1
            if y < H:
                new_arr = [r[:] for r in arr]
                boom(y, x, new_arr)
                drop(new_arr)
                dfs(lev + 1, new_arr)
            else:
                dfs(lev + 1, arr)


    # 실행
    T = int(input())
    for tc in range(1, T + 1):
        N, W, H = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(H)]
        dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
        mx = 0
        dfs(0, arr)
        print(f"#{tc} {W * H - mx}")
