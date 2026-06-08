# 오늘은 bfs
#
#
# 증가하는 사탕수열
# 전봇대
#
# bfs -> 플러드필(bfs를 좌표에 적용)
# 파이프(탈주범 검거), 벽돌 꺠기


#
# bfs -> 플러드필 (bfs를 좌표에 적용)
# 파이프 (탈주범 검거) -> level 단위로 탐색 (floodfill),
# 벽돌 꺠기 -> 폭탄이 퍼져나가는 형태 (floodfill)




############################################################################################
# 증가하는 사탕수열
############################################################################################
#
# 3가지 경우 -> 함수로 만들어서 return 처리
#
# 1. 이미 만족하는 경우 return 0
#
# 2. 사탕을 먹고 조건에 만족하면 return eat_A + eat_B
#
# 3. 조건에 만족하지 않으면 return -1
#
# def first(a, b, c):
#     if a < b< c and a >= 1:
#         return 0
# #
# # cnt = 0
# # def second(a, b, c):
# #     global cnt
# #     while b > c:
# #         b -= 1
# #         cnt +=1
# #         if b < c:
# #             continue
# #     while a > b:
# #         a -= 1
# #         cnt +=1
# #         if a > b:
# #             continue
# #         return cnt
# #
# # def third(a, b, c):
# #     if a<0 or b<2 or c<3:
# #         return -1
# #
# #
#

# 강사님 코드
#
# def get_eating(A, B, C):
#     # 1. 이미 만족 하는 경우
#     if A < B < C:
#         return 0
#
#
#     # 사탕 개수 계산
#     # 예를 들어
#     # B = 5, C = 5  |  B - ( C- 1 ) 개 먹어야 함
#
#     eat_B = max(0, B - C + 1)
#     new_B = B - eat_B
#
#     eat_A = max( 0, A - new_B +1)
#     new_A = A - eat_A
#
#
#     # 2. 조건을 만족하는지 확인 if - else
#     if 0< new_A < new_B < C:
#         return eat_A + eat_B
#
#     else:  # 3. 조건을 만족하지 않는 경우
#         return -1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     A, B, C = map(int, input().split())
#     result = get_eating(A, B, C)
#
#
#     print(f"#{tc} {result}")
#
#
#
#
#
#
#
# def solve(a, b, c):
#     if a< b< c and a >= 1:
#         return 0
#     if a< 1 or b <2 or c < 3:
#         return -1
#
#     cnt = 0
#     if b >= c:
#         cnt += b - c +1
#         b -= cnt
#
#     if a >= b :
#         cnt += a - b +1
#         a -= cnt
#
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T+1):
#     a, b, c = map(int, input().split())


    # print(f"#{tc} {solve(a, b, c)}")







############################################################################################
# 전보대
###########################################################################################

#
# def cntgogo(start, end):
#     cnt = 0
#     for prev_start, prev_end in stack:
#         if start < prev_start and end > prev_end:
#             cnt += 1
#         if start > prev_start and end < prev_end:
#             cnt += 1
#
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#
#     stack = []
#     total= 0
#     for _ in range(N):
#         start, end = map(int, input().split())
#         total += cntgogo(start, end)
#
#         stack.append([start,end])
#
#
#     print(f"#{tc} {total}")


# ＃＃＃？？
# 　
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     stack = []
#     cnt = 0
#     for _ in range(N):
#         start, end = map(int, input().split())
#         stack.append([start, end])
#
#         for prev_start, prev_end in stack:
#             if end < prev_end:
#                 cnt +=1
#
#
#
#     print(f"#{tc} {cnt}")
#
#







# bfs 탐색과정
# 1. 큐에서 뺀다 (탐색)
#     popleft()
#
# 2. 다음 갈 수 있는 노드 예약걸기(큐 등록)
#     append()
#
# from collections import deque
#
# alist = [[] for _ in range(7)]
#
# alist[0] = [1, 2]
# alist[1] = [3]
# alist[2] = [4]
# alist[4] = [5, 6]
#
# q = deque()
# q.append(0) # start지점
#
# name = "ABCDEFG"
#
# while q: # 큐가 빌때 까지 반복
#     # 1. 큐에서 뺀다(탐색) - popleft()
#     now = q[0]
#     q.popleft()
#     print(name[now], end = ' ')
#
#     # 2. 다음 갈곳 예약 걸기(큐 등록) - append()
#     for i in range(len(alist[now])):
#         next = alist[now][i]
#         q.append(next)
#
#


################### 시작 1

#
# from collections import deque
#
# def bfs(start):
#     q = deque()
#     used = [0] * 6
#
#     q.append(start)
#     used[start] = 1
#
#     while q:
#         # 1. 큐에펏 뺸다 (탐색)
#         now = q[0]
#         print(chr(now + ord('A')), end = ' ')
#         q.popleft()
#
#         for i in range(len(alist[now])):
#
#             next = alist[now][i]
#             # 이미 탐색했으면 continue
#             if used[next] == 1: continue
#             # 방문표시
#             used[next] = 1
#             q.append(next) #예약걸기
#             # 방문기록 지우지 x
#
# alist = [[] for _ in range(6)]
# alist[0] = [1, 2]
# alist[1] = [0, 2]
# alist[2] = [0, 1, 3]
# alist[3] = [2, 4]
# alist[4] = [3]
#
# n = int(input())
# bfs(n)
#
#
# ######################### final

# from collections import deque
#
# MAP = [
#     [0, 1, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [1, 0, 0, 0, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0]
#
# ]
#
# q = deque()
# used = [0] * 5
# start, end = map(int, input().split())
# # start 노드 q에 넣어주고,
# # level도 같이 넣어준다. q.append((node, level))
#
#
# q.append((start, 0))
# used[start] = 1 # 시작노드 방문처리
#
# while q:
#     # 1. 큐에서 뺸다 (탐색)
#     now, level = q[0]
#     q.popleft()
#
#
#     # now가 end에 도착했을때  break
#     if now == end:
#         print(level)
#         break
#
#     # 2. 다음 갈 곳 예약 걸기 (큐에 등록)
#
#     for i in range(5):
#         if MAP[now][i] == 0: continue
#         if used[i] == 1: continue
#         used[i] = 1
#         q.append((i, level + 1))










############################################################################
# 플러드필
# bfs + 좌표 (방향배열)
############################################################################

from collections import deque

visited = [[] * 5 for _ in range(5)]

# 방향배열

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def flood_fill(start_y, start_x):
    q = deque()
    q.append((start_y,start_x)) # 시작 좌표를 큐에 추가
    visited[start_y][start_x] = 1  # 시작 좌표를 방문 처리

    while q:
        # 1. 큐에서 뺀다
        now_y, now_x = q.popleft()
        # 2. 다음 갈 곳 예약 걸기
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5: continue

            # 이미 방문했으면 continue
            if visited[ny][nx] != 0: continue

            # 큐 등록 + 거리 업데이트
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))


# 함수 호출
sty, stx = map(int, input().split())
flood_fill(sty,stx)


# 결과 출력
for y in range(5):
    for x in range(5):
        print(visited[y][x], end = " ")
    print()

for y in range(5):
    print(*visited[y])



# 플러드필
# bfs + 좌표(방향배열)
from collections import deque

# 5x5 행렬
visited = [[0] * 5 for _ in range(5)]

# 방향 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def flood_fill(start_y, start_x):
    q = deque()
    q.append((start_y, start_x)) # 시작 좌표를 큐에 추가
    visited[start_y][start_x] = 1 # 시작 좌표를 방문 처리

    while q:
        # 1. 큐에서 뺀다(탐색)
        now_y, now_x = q.popleft()
        # 2. 다음 갈곳 예약 걸기
        for i in range(4): # 4방향
            ny = now_y + dy[i]
            nx = now_x + dx[i]

            # 방향배열 범위체크 (좌표 범위체크)
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5: continue

            # 이미 방문했으면 continue
            if visited[ny][nx] != 0: continue

            # 큐 등록 + 거리 업데이트
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))


# 함수 호출
sty, stx = map(int, input().split())
flood_fill(sty, stx)

# 결과 출력
for y in range(5):
    for x in range(5):
        print(visited[y][x], end = " ")
    print()






# 자료구조!
# pipe 의 모든 경우 [상, 하, 좌, 우] -> 8개의 경우

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

types = {
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












# T = int(input())
#
# for tc in range(1, T+1):
#     N, M, R, C, L = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]





