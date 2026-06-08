#
# # 플러드필
# # bfs + 좌표(방향배열)
# from collections import deque
#
# # 5x5 행렬
# visited = [[0] * 5 for _ in range(5)]
#
# # 방향 배열
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def flood_fill(start_y, start_x):
#     q = deque()
#     q.append((start_y, start_x)) # 시작 좌표를 큐에 추가
#     visited[start_y][start_x] = 1 # 시작 좌표를 방문 처리
#
#     while q:
#         # 1. 큐에서 뺀다(탐색)
#         now_y, now_x = q.popleft()
#         # 2. 다음 갈곳 예약 걸기
#         for i in range(4): # 4방향
#             ny = now_y + dy[i]
#             nx = now_x + dx[i]
#
#             # 방향배열 범위체크 (좌표 범위체크)
#             if ny < 0 or nx < 0 or ny >= 5 or nx >= 5: continue
#
#             # 이미 방문했으면 continue
#             if visited[ny][nx] != 0: continue
#
#             # 큐 등록 + 거리 업데이트
#             visited[ny][nx] = visited[now_y][now_x] + 1
#             q.append((ny, nx))
#
#
# # 함수 호출
# sty, stx = map(int, input().split())
# flood_fill(sty, stx)
#
# # 결과 출력
# for y in range(5):
#     for x in range(5):
#         print(visited[y][x], end = " ")
#     print()






from collections import deque


# 자료구조!
# pipe 의 모든 경우 [상, 하, 좌, 우] -> 8개의 경우

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

pipe = {
    # 상하좌우 순서로 기록
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

# 다음 칸으로 연결되는 파이프의 방향
# 상, 하, 좌, 우 : 0, 1, 2, 3
# 상 -> 하, 하 -> 상, 좌 -> 우, 우 -> 좌

opp = [1, 0, 3, 2]



def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)] # N x M 행렬
    q.append((R, C)) # 시작 위치 큐에 추가
    visited[R][C] = 1 # 시작 노드 방문 표시
    cnt = 1

    while q:
        # 1. 큐에서 뺀다(탐색)
        y, x = q.popleft()

        # 언제 cnt 반환할까
        # 시간이 L에 도달하면 cnt 반환
        if visited[y][x] == L:
            return cnt


        # 4방향
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 좌표범위안에, 방문하지 않아야하고, 파이프가 연결w되었는지 (현재 파이프 and 다음파이프)
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and pipe[arr[y][x]][i] and pipe[arr[ny][nx]][opp[i]]:
                # 2. 다음갈 곳 예약 걸기
                q.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1#방문 표시
                cnt +=1

    return cnt # 총 방문한 칸수 반환


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L =map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = bfs()
    print(f"#{tc} {result}")

    # from collections import deque
    #
    # # 자료구조!
    # # pipe의 모든 경우 [상, 하, 좌, 우] -> 8개의 종류
    # pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0],
    #         [1, 0, 1, 0]]
    # # 델타배열(방향배열) : 상 하 좌 우
    # dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    # # 다음칸으로 연결되는 파이프의 방향은 반대방향이어야 한다
    # # 상, 하, 좌, 우 : 0, 1, 2, 3
    # # 상 -> 하, 하 -> 상, 좌 -> 우, 우 -> 좌
    # opp = [1, 0, 3, 2]
    #
    #
    # def bfs():
    #     q = deque()
    #     visited = [[0] * M for _ in range(N)]  # NxM행렬
    #     q.append((R, C))  # 시작 위치 큐에 추가
    #     visited[R][C] = 1  # 시작 노드 방문 표시
    #     cnt = 1
    #
    #     while q:
    #         # 1. 큐에서 뺀다(탐색)
    #         y, x = q.popleft()
    #
    #         # 언제 cnt 반환할까?
    #         # 시간이 L에 도달하면 cnt 반환
    #         if visited[y][x] == L:
    #             return cnt
    #
    #         # 4방향
    #         for i in range(4):
    #             ny, nx = y + dy[i], x + dx[i]
    #             # 좌표범위안에, 방문하지 않아야하고, 파이프가 연결 되었는지(현재파이프 and 다음파이프)
    #             if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and pipe[arr[y][x]][i] and pipe[arr[ny][nx]][
    #                 opp[i]]:
    #                 # 2. 다음갈곳 예약 걸기
    #                 q.append((ny, nx))
    #                 visited[ny][nx] = visited[y][x] + 1  # 방문표시
    #                 cnt += 1
    #
    #     return cnt  # 총 반문한 칸수 반환
    #
    #
    # T = int(input())
    # for tc in range(1, T + 1):
    #     N, M, R, C, L = map(int, input().split())
    #     arr = [list(map(int, input().split())) for _ in range(N)]
    #     result = bfs()
    #     print(f'#{tc} {result}')