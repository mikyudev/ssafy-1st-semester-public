# import sys
# sys.stdin = open("1953.txt")
#
# ########################################################################
# # 지도 - 이차원 배열 형태
#
# # 맨홀 뚜껑으로 부터 출발
#  # 터널들의 이동
#  # 이동방향 : 상하좌우
#  #  -> 델타배열
#  #     - 이동못하는 경우가 존재
#
#
#
#
# # 시작점으로 주변으로 점점 퍼져나가면서확인 (BFS)
# # BFS
# #  Queue를 활용해서 먼저 확인하는 노드부터 먼저 확인하자
# #  먼저 방문한 노드에서 갈 수 있는 노드들을 후보군(queue)에 추가
#
#  # O( V + E)
#  #  V : 정점의 개수 / E : 간선의 개수
#  # 정점의 개수 = 2500개 (50*50
#   # queue 에 2500까지 들어갈 수 있따. -> 여유롭구몬수학
#    # 간선의 개수 = 2500 * 4 (상하좌우) = 10000개
#
#
# ########################################################################
#
#
# # 1. bfs로 접근
# #   - 이동 방향: 상하좌우
#
# #   - 이동이 불가능한 케이스
# #   - [델타 범위 기본] 범위 밖으로 나가면 못감
# #   - [방문 기록 기본] 이미 방문한 곳은 못감
#
# #  ++++ 0이면 못간다
#
#
# #   - [문제 조건]
# #     현재 내 위치에서 뚫려있는 곳만 이동가능
# #     다음 위치의 입구가 뚫려있는 곳으로만 가능
# #      -> 이런 케이스들은 델타배열과 동일한 순서 (상하좌우)
# #                  이동 가능 여부를 기록해두면 좋다.
# # 2. 방문 기록을 해야한다 (visited)
#
#
# # 델타배열
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
#
# types = {
#     1: [1, 1, 1, 1],
#     2: [1, 1, 0, 0],
#     3: [0, 0, 1, 1],
#     4: [1, 0, 0, 1],
#     5: [0, 1, 0, 1],
#     6: [0, 1, 1, 0],
#     7: [1, 0, 1, 0]
# }
#
#
#
#
# def bfs(R, C):
#     q = [(R, C)] # 후보군
#     visited[R][C] = 1 # 출발점 초기화
#
#
#     while q:  # 후보군이 없을 떄 까지(더 이상 방문할 수 있는 곳이 없으면 종료)
#         now_y, now_x = q.pop(0)
#         dirs = types[graph[now_y][now_x]]
#
#
#         for dir in range(4): # 상하좌우 확인
#             # 출구가 없으면 다음 방향 확인 (continue)
#             if dirs[dir] == 0:
#                 continue
#
#
#             # 다음 좌표
#             new_y = now_y + dy[dir]
#             new_x = now_x + dx[dir]
#
#             # 범위 밖이면 pass
#             if new_y <0 or new_x <0 or new_y >= N or new_x >=N:
#                 continue
#
#             if graph[new_y][new_x] == 0:
#                 continue
#             # 이미 방문했으면 pass
#             if visited[new_y][new_x]:
#                 continue
#             # 다음 좌표 터널 뚫린것을 확인
#             next_dirs = types[graph[new_y][new_x]]
#
#             # 현재 상좌 -> next_dirs가 하우 가 안 뚫렸으면 못간다
#             if dir % 2 == 0 and next_dirs[dir + 1] == 0:
#                 continue
#
#
#             # 현재 하우 -> next_dirs의 상좌가 안뚫렸르면 못간다
#             if dir % 2 == 1 and next_dirs[dir - 1] == 0:
#                 continue
#
#
#             # 시간을 +1 해주면서 기록
#             visited[new_y][new_x] = visited[now_y][now_x] +1
#             q.append((new_y,new_x))
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M, R, C, L = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(N)]
#
#
#     visited = [[0] * N for _ in range(M)]
#
#
#     bfs(R, C)
#     cnt = 0
#     # L시간 이하로 방문한 곳
#     for i in range(N):
#         for j in range(M):
#             if 0 < visited[i][j] <= L:
#                 cnt += 1
#
#     print(f"#{tc} {cnt}")
#
#
#
#
#
#
alist = list([] for _ in range(7))
#
alist[5] = [3, 1]  # 2번 반복 alist[now][i]
alist[3] = [2]  # 1반복 alist[now][i]
alist[1] = [4]
alist[4] = [0, 6]

print()
print(alist, end = ' ')