########################################################################
# 장훈이
# 1
# 5 16
# 3 1 3 5 6
########################################################################

# 1- 3 , 3- 1 같은 집합 (순열 x, 중복순열 x )
# n 명을 뽑아야 한다. 조합 x

# 이거 부분집합임   ==> 비트연산으로 풀어봅시다


# 1. 부분집합 핵심 로직 : 비트연산

    # for i in range(N):
    #     if tar & 0x1: # 마지막 비트가 1인지 확인
    #         sum_v += heights[i]
    #
    #     tar >>= 1 # target을 오른쪽으로 밀면서
    #
    # # 우리가 구하려는건 높이의 최소값 x -> 차이의 최소값
    #
    # diff = sum_v - B


########################################################################
########################################################################

# def get_sum(tar):
#     sum_v = 0
#     for i in range(N):
#         if tar & 0x1:
#             sum_v += heights[i]
#         tar >>= 1
#     return sum_v
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())
#     heights = list(map(int, input().split()))
#     min_diff = float('inf')
#
#     for tar in range(1, 1<<N): # 2의 n제곱 개
#         total = get_sum(tar)
#         if total >= B:
#             diff = total - B
#             min_diff = min(diff, min_diff)
#
#
#     print(f"#{tc} {min_diff}")
########################################################################
########################################################################




########################################################################
# 수영장
########################################################################

# 완전탐색, 재귀호출
# branch = 4
# level

########################################################################
# 이게 기저조건
# def recur(month):
#     if month > 12:
#         result = min(result, sum_v)
#         return
########################################################################





#
# def recur(month, sum_v):
#     global result
#     if month >= 12:
#         result = min(result, sum_v)
#         return
#
#     recur(month + 1, sum_v + days[month] * day)
#     recur(month + 1, sum_v + month1)
#     recur(month + 3, sum_v + month3)
#     recur(month + 12, sum_v + year)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     day, month1, month3, year = map(int, input().split())
#     days= list(map(int, input().split()))
#     result = float('inf')
#
#     recur(0,0)
#     print(f"#{tc} {result}")




########################################################################
# 격자판의 숫자 이어 붙이기
########################################################################

# 1. 상 하 좌 우 (방향배열)
#
# 2. ny, nx dfs
# dfs ( ny, nx, sum_v + arr[ny][nx])
#
# 3. 기저조건 숫자가 7자리가 되면 return
#
# 4. 중복제거 set()
# result.add(sum_v)


#
#
#
# やハロー = [-1, 1, 0, 0]
# ワンワン = [0, 0, -1, 1]
#
# def miku(ニャン, にゃんにゃん, 魔法):
#     if len(魔法) == 7:
#         応援.add(魔法)
#         return
#
#
#
#     for i in range(4):
#         初音ミク = ニャン + やハロー[i]
#         テト = にゃんにゃん + ワンワン[i]
#         if 初音ミク < 0 or テト < 0 or 初音ミク >= len(ドラえもん) or テト >= len(ドラえもん): continue
#
#
#         miku(初音ミク, テト, 魔法 + ドラえもん[初音ミク][テト])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     ドラえもん = [input().split() for _ in range(4)]
#
#     応援 = set()
#     for スタートｙ in range(len(ドラえもん)):
#         for すたーとｘ in range(len(ドラえもん)):
#             miku(スタートｙ, すたーとｘ, ドラえもん[スタートｙ][すたーとｘ])
#
#
#
#     print(f"#{tc} {len(応援)}")
#
#
#
#
#
#
# ########################################################################
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def dfs(y, x, sum_v):
#     # 길이가 7이면 return ( 기저조건)
#     if len(sum_v) == 7:
#         result.add(sum_v) # 세트(중복제거)
#         return
#
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#
#         if ny < 0 or nx < 0 or nx >= 4 or nx >= 4:
#             continue
#
#         dfs(ny, nx, sum_v + arr[ny][nx])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = [input().split() for _ in range(4)]
#     result = set()
#     # 시작지점
#
#     for y in range(4):
#         for x in range(4):
#             dfs(y, x, arr[y][x])
#
#



########################################################################
########################################################################





# dy = [-1, 1, 0, 0]
# dx= [0, 0, -1, 1]
#
# for i in range(4):
#     ny, nx = y + dy[i], x + dx[i]
#
#
#     cnt += 1
#     dfs(ny, nx)




########################################################################



#
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    best_start = float('inf')
    max_v = 0


    for y in range(N):
        for x in range(N):
            current_y = y
            current_x = x
            cnt = 1

            while True:
                next_y, next_x = -1, -1

                for i in range(4):
                    ny = current_y + dy[i]
                    nx = current_x + dx[i]
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue

                    if arr[ny][nx] == arr[current_y][current_x] + 1:
                        next_y,next_x = ny, nx
                        break


                if next_y != -1:
                    current_y, current_x = next_y, next_x
                    cnt+=1
                else:
                    break

            # start_v = arr[y][x]
            # if cnt > max_v or (cnt == max_v and start_v < best_start):
            #     max_v = cnt
            #     best_start = start_v


            start_v = arr[y][x]  # ← 반드시 출발점 기준!
            if cnt > max_v:
                max_v = cnt
                best_start = start_v
            elif cnt == max_v and start_v < best_start:
                best_start = start_v


    print(f"#{tc} {best_start} {max_v}")
#
#
#
#