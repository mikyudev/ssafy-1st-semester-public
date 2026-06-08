# 순열 : 중복없이, 순서를 고려하여 나열한 것 예시) 달리기 시합 1,2,3등
# 즉 (1, 2)와 (2, 1)은 다른 순열이다

# 중복순열 : 중복을 허용한 순열
# (0, 0) (1, 1) 모두 허용

################################

################################

# branch = 3
# level = 2 중복순열
#
# path = []
# def recur(lev):
#     if lev == 2:
#         print(path)
#         return
#     for i in range(3):
#         path.append(i)
#         recur(lev + 1)
#         path.pop()
# recur(0)

################################
# 처음 사용한 숫자는 used에 기록, 백트래킹 될 때 used기록을 지워준다
# 숫자 다시 사용해야하니까

################################
#
# path = []
# used = [0]* 3
# def recur(lev):
#     if lev == 2: # level 2
#         print(path)
#         return
#     for i in range(3): # branch 3
#         if used[i] == 1: # 이미 사용한 숫자면 continue
#             continue
#         used[i] = 1
#         path.append(i)
#         recur(lev + 1)
#         path.pop()
#         used[i] = 0
# recur(0)
#

######################################################################################
# 부분집합 코드는 branch가 2인 중복순열 코드와 같다. ex) 영화관에 가려는데 누구를 데려갈지
# 뽑을지 안 뽑을지
######################################################################################

# 집합의 총 개수는 2ⁿ

# 비트연산 : 1 << n !!!!!!

# ex) 1 << 3 : 1을 왼쪽으로 3번 밀어라 => 1000(2진수) -> 2³

# 2. 왼쪽으로 한 번씩 밀면서 마지막 비트가 1인지 0인지 확인
# !!!!!!!!
# for i in range(n):
#     if tar & 0x1: #마지막 비트가 1인지 확인
#         print(arr[i], end=' ')
#     tar >>= 1


# arr = ['A', 'B', 'C']
# n = len(arr)
#
# def get_sum(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end = '')
#         tar >>= 1
#
#
# for tar in range(1 << n):
#     print('{', end='')
#     get_sum(tar)
#     print('}')



######################################################################################
# 5명중에 3명을 뽑는 조합(순서는 고려하지 x)
# a,b,c 와 c,b,a 는 같은 조합

# ######################################################################################
# arr = ['A','B','C','D','E']
#
# for i in range(5):
#     start1 = i +1
#     for j in range(start1, 5): #branch가 최대 5
#         start2 = j +1
#         for z in range(start2, 5): #branch가 최대 5
#             print(arr[i], arr[j], arr[z])
#
#
#
# arr = ['A','B','C','D','E']
# path = []
# n = 3
# # # 5명중에 3명을 뽑늗 ㅏ
#
# def recur(lev, start):
#     if lev == n: # level 은 n 명을 뽑느다
#         print(*path)
#         return
#
#     for i in range(start, 5): # branch가 최대 5
#         path.append(arr[i])
#         recur(lev + 1, i + 1)
#         path.pop()
#
# recur(0, 0)










#

#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     dy=[0,1]
#     dx=[1,0]
#
#     for y in range(N):
#         for x in range(N):
#             current_y, current_x = y, x
#
#     total = 0
#     while arr[N][N]:
#         for i in range(N):
#             for j in range(N)
#






## baby_gin

1.
# level = 6  카드 6장을 뽑는다
# branch = 6  6개의 순열을 만든다

#  2. 중복순열 vs 순열
#  순열이기 때문에 used 배열 사용

#  3. bab_gin 판별 함수 만들기 return (cnt == 2)
# 3-1. 앞에 세자리가 triplet 또는 run이라면 cnt += 1
# 3-2. 뒤에 세자리가 triplet 또는 run 이라면 cnt += 1

# arr = list(map(int, input().split()))


# arr = input().split()


# branch = 3
# lev = 2
#
# path = []
# used = [0]*len(arr)
# def baby_gin(lev,start):
#     if lev == 6:
#         print(path)
#         return
#     for i in range(start, 10):
#         path.append(arr[i])
#         baby_gin(lev + 1, i+1)
#         path.pop()
# baby_gin(0, 0)
#
#
#








#
#
# arr = list(map(int,input().split()))
# N = 6
#
# path = [0]*N
# used = [0]*N
# is_found = False
#
# def check_baby_gin(cards):
#
#     front_is_gin = False
#     if cards[0] == cards[1] and cards[1] == cards[2]:
#         front_is_gin = True
#
#     if cards[0]+1 == cards[1] and cards[1] + 1 == cards[2]:
#         front_is_gin = True
#
#     back_is_gin = False
#     if cards[3] == cards[4] and cards[4] ==cards[5]:
#         back_is_gin = True
#     if cards[3] + 1 == cards[4] and cards[4] + 1 == cards[5]:
#         back_is_gin = True
#
#
#     if front_is_gin and back_is_gin:
#         return True
#
#     else:
#         return False
#
# def generate_permutations(level):
#     global is_found
#     if is_found:
#         return
#
#     if level==N:
#         if check_baby_gin(path):
#             is_found = True
#         return
#
#     for i in range(N):
#         if used[i] == 0:
#             used[i] = 1
#             path[level] = arr[i]
#             generate_permutations(level + 1)
#             used[i] = 0
#
# generate_permutations(0)
#
#
# if is_found:
#     print("Yes")
# else:
#     print("No")
#




#
#
#
#
# used = [0] * 6
# path = []
# is_babygin = 0
# def is_baby_gin():
#     cnt = 0
#     # 앞에 세자리가 triplet 또는 run
#     a, b, c = path[0], path[1], path[2]
#     if a == b == c: cnt += 1
#     elif (a) == (b-1) == (c-2) : cnt += 1
#
#     # 뒤에 세자리가 triplet 또는 run
#     a, b, c = path[3], path[4], path[5]
#     if a == b == c: cnt += 1
#     elif (a) == (b-1) == (c-2) : cnt += 1
#
#     return cnt == 2 # cnt가 2면 babygin이 맞다!
#
# # 순열코드
# def recur(lev):
#     global is_babygin
#     if lev == 6: # level은 6
#         if is_baby_gin():
#             is_babygin = 1
#         return
#
#     for i in range(6): # branch 는 6
#         if used[i] == 1: continue
#         used[i] = 1
#         path.append(arr[i])
#         recur(lev +1)
#         path.pop()
#         used[i] = 0
#
# arr = list(map(int, input().split()))
# recur(0)


#
# ###############################################################
# if is_babygin:
#     print("Yes")
# else:
#     print("No")
#
#
# used = [0] * 6
# path = []
# is_babygin = 0
#
# def is_baby_gin():
#     cnt = 0
#     # 앞에 세자리가 triplet 또는 run
#     a, b, c = path[0], path[1], path[2]
#     if a == b == c: cnt += 1
#     elif (a) == (b - 1) == (c - 2) : cnt += 1
#
#     # 뒤에 세자리가 triplet 또는 run
#     a, b, c = path[3], path[4], path[5]
#     if a == b == c: cnt += 1
#     elif (a) == (b - 1) == (c - 2) : cnt += 1
#
#     return cnt == 2 # cnt 가 2면 baby-gin이 맞다!
#
# # 순열 코드
# def recur(lev):
#     global is_babygin
#     if lev == 6: # level은 6
#         if is_baby_gin():
#             is_babygin = 1
#         return
#
#     for i in range(6): # branch는 6
#         if used[i] == 1: continue
#         used[i] = 1
#         path.append(arr[i])
#         recur(lev + 1)
#         path.pop()
#         used[i] = 0
#
# arr = list(map(int, input().split()))
# recur(0)
#
# if is_babygin: print('Yes')
# else: print('No')











###################################################################################
#  최소합 (dfs 문제임)
###################################################################################
#
# 좌표를 이동할때 dfs호출
#
# 1-1 오른쪽으로 이동 할 때 dfs호출
# 1-2 아래로 이동 할 때 dfs호출
#
# 2. 정점 노드에 도달하면 return (좌표 끝 - 우측 하단)
#     if
#
#
#
#
#
#
#
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     total1 = 0
#     for i in range(N):
#         total1 += arr[i][0]
#     for j in range(N):
#         total1 +=arr[N-1][j]
#     total1 -= arr[N-1][0]
#
#     total2 = 0
#     for i in range(N):
#         total2 += arr[0][i]
#     for j in range(N):
#         total2 += arr[j][N-1]
#     total2 -= arr[0][N-1]
#
#     min_v = float('inf')
#     min_v = min(min_v, total2, total1)
#
#     print(f"#{tc} {min_v}")



# dfs로 풀건데 그러면 dfs재귀호출을 언제할거냐??
# 좌표를 이동할때 dfs호출
#
# 1-1. 오른쪽으로 이동 할때 dfs호출 dfs(y, x, sum_v)
# 1-2. 아래로 이동 할때 dfs 호출 dfs(y, x, sum_v)
#
# 2. 정점 노드에 도달하면 return (좌표 끝 - 우측 하단)
#     if y == N - 1 and x == N - 1:
#     최소값 갱신(min_sum)
#         return
#
# 3. 가지치기 (sum_v를 재귀호출 할때마다 갱신)


## 제미나이
#     sum_v >= min_sum -> 가지치기
# 재귀 깊이 제한을 풀어줍니다 (N이 클 경우를 대비)



# DFS 함수 정의
# y, x: 현재 좌표
# current_sum: (y,x)까지의 누적 합계
# def dfs(y, x, current_sum):
#     global min_v
#
#     # --- 3. 가지치기 ---
#     # 현재까지의 합이 이미 이전에 찾은 최소합보다 크면,
#     # 이 경로는 더 이상 탐색할 가치가 없으므로 중단합니다.
#     if current_sum >= min_v:
#         return
#
#     # --- 2. 종료 조건 ---
#     # 오른쪽 맨 아래에 도달했을 때
#     if y == N - 1 and x == N - 1:
#         # 현재 경로의 합계가 최소합보다 작으면 갱신합니다.
#         min_v = min(min_v, current_sum)
#         return
#
#     # --- 1. 재귀 호출 (경로 탐색) ---
#     # 오른쪽이나 아래로 이동하며 다음 경로를 탐색합니다.
#     # 다음 좌표가 격자 범위 안에 있을 때만 이동합니다.
#
#     # 아래로 이동
#     if y + 1 < N:
#         dfs(y + 1, x, current_sum + arr[y + 1][x])
#
#     # 오른쪽으로 이동
#     if x + 1 < N:
#         dfs(y, x + 1, current_sum + arr[y][x + 1])
#
#
# # --- 메인 실행 부분 ---
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 최소 합계를 저장할 변수 (아주 큰 값으로 초기화)
#     min_v = float('inf')
#
#     # DFS 탐색 시작
#     # 시작점 (0,0)에서 출발하며, 시작점의 값(arr[0][0])을 초기 합계로 가집니다.
#     dfs(0, 0, arr[0][0])
#
#     print(f"#{tc} {min_v}")


#
# def dfs(y, x, sum_v):
#     global min_sum
#     # 좌표 끝에 도달 했을때(정점 노드에 도달 했을 때)
#     if y == N-1 and x == N -1:
#         # 최소값 갱신하고 return
#         min_sum = min(min_sum, sum_v)
#
#     # 가지치기
#
#     if sum_v >= min_sum:
#         return
#
#     # 오른쪽으로 이동
#     if x < N - 1:
#         dfs(y, x+1, sum_v + arr[y][x + 1])
#
#     # 아래로 이동
#     if y < N - 1:
#         dfs(y+1, x, sum_v + arr[y + 1][x])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     min_sum = float('inf')
#
#     dfs(0,0, arr[0][0])
#
#     print(f"#{tc} {min_sum}")





###################################################################################
# 골프장
###################################################################################
#


# 1. branch, level : N-1

# 2. 음수인덱스
# 마지막 구역에서 사무실로 돌아오는 비용
# arr[path[-1]][0]

# 3. 마지막 방문 지점의 이전에 방문한 지점
# arr[path[-2]][i]



# def glof(y,x,sum_v)
#
#
#
#
# path = []
# used = [0]* 3
# def recur(lev):
#     if lev == 2: # level 2
#         print(path)
#         return
#     for i in range(3): # branch 3
#         if used[i] == 1: # 이미 사용한 숫자면 continue
#             continue
#         used[i] = 1
#         path.append(i)
#         recur(lev + 1)
#         path.pop()
#         used[i] = 0
# recur(0)

#
# def find_path(current, level, battery_sum):
#     global min_v
#
#     if battery_sum >= min_v:
#         return
#
#     # 모든 관리구역을 다 방문했다면
#     if level == N - 1:
#         # 마지막 구역에서 사무실(0)로 복귀하는 배터리 양을 더함
#         total_sum = battery_sum + arr[current][0]
#         min_v = min(min_v, total_sum)
#         return
#
#     # 다음 방문할 구역(1번부터 N-1번)을 찾는다
#     for next_node in range(1, N):
#         if visited[next_node] == 1: continue
#         visited[next_node] = 1
#
#         # ★★★ 바로 이 부분! ★★★
#         # 다음 장소(next_node)로 이동하면서,
#         # 지금까지의 합계(battery_sum)에 현재 이동량(arr[current][next_node])을 더해서
#         # 다음 재귀 함수에 넘겨줍니다.
#         find_path(next_node, level + 1, battery_sum + arr[current][next_node])
#
#         # 백트래킹
#         visited[next_node] = False
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     path = []
#     min_v = float('inf')
#     visited = [0]*N
#     find_path(0, 0, 0)
#
#     print(f"#{tc} {min_v}")
#



def dfs(lev, sum_v):
    global min_v

    if lev == N - 1:
        sum_v += arr[path[-1]][0]
        min_v = min(min_v, sum_v) # 최소값 갱신
        return

    for i in range(1, N): # branch N-1
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(i)
        dfs(lev + 1, sum_v + arr[path[-2]][i])
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [0] # 사무실 (0)에서 시작
    used = [0] * N
    used[0] = 1 # 사무실 방문처리
    min_v = float('inf')
    dfs(0,0)
    print(f"#{tc} {min_v}")