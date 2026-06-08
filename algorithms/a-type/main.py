### 부분집합





# T = int(input())
# for tc in range(1, T+1):
#     N, p = map(int, input().split())
#     A = [0] + list(map(int, input().split()))
#     B = [0] + list(map(int, input().split()))
#
#     dpA = [0] * (N + 1)
#     dpB = [0] * (N + 1)
#
#     dpA[1] = A[1]
#     dpB[1] = B[1]
#     for i in range(2, N+1):
#         dpA[i] = max(dpA[i-1] + (A[i]-p), dpB[i-1] + A[i])
#         dpB[i] = max(dpB[i-1] + (B[i]-p), dpA[i-1] + B[i])
#
#     print(f"#{tc} {max(dpA[N], dpB[N])}")  # 18
#
# #################################################################
# #
# T = int(input())
# for tc in range(1, T+1):
#     n, p = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#
#     dpA = [0] * (n)
#     dpB = [0] * (n)
#
#     dpA[0] = A[0]
#     dpB[0] = B[0]
#
#     for i in range(1, n):
#         dpA[i] = max(dpA[i-1] + (A[i] - p), dpB[i-1] + A[i])
#         dpB[i] = max(dpB[i-1] + (B[i] - p), dpA[i-1] + B[i])
#
#     print(f"#{tc} {max(dpA[-1], dpB[-1])}")

#################################################################
#################################################################
# T, N, p, A, B 등 초기 설정은 동일
# ...

# 재귀 함수 정의
def solve(k, prev_choice):
    # 기본 사례(Base Case): 모든 화분을 다 봤으면 0점
    if k == n:
        return 0

    # k번째 화분이 받을 벌칙 계산
    penalty = 0
    if prev_choice == 'A':  # 바로 직전에 A비료를 줬다면
        penalty = p

    # 선택 1: k번째에 A비료를 선택할 경우
    # (k번째 성장량) + (k+1부터 끝까지 얻을 최대 점수)
    score_A = (A[k] - penalty) + solve(k + 1, 'A')



    # 선택 2: k번째에 B비료를 선택할 경우
    score_B = (B[k] - penalty) + solve(k + 1, 'B')

    # 두 선택지 중 더 좋은 결과를 반환
    return max(score_A, score_B)

# --- 메인 로직 ---
# # 0번째 화분 이전에는 아무 선택도 없었다고 가정하고 'B'를 넘겨줌 (벌칙 없음)
# T = int(input())
# for tc in range(1, T+1):
#     n, p = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     answer = solve(0, 'B')
#     print(f"#{tc} {answer}")





T = int(input())
for tc in range(1, T+1):
    n, p = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dpA = [0] * (n)
    dpB = [0] * (n)

    dpA[0] = A[0]
    dpB[0] = B[0]

    for i in range(1, n):
        dpA[i] = max(dpA[i-1] + (A[i] - p), dpB[i-1] + A[i])
        dpB[i] = max(dpB[i-1] + (B[i] - p), dpA[i-1] + B[i])

    print(f"#{tc} {max(dpA[-1], dpB[-1])}")















T = int(input())
for tc in range(T):
    N, p = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    dpA = [0] * N
    dpB = [0] * N

    dpA[0] = A[0]
    dpB[0] = B[0]


    for i in range(1, N):
        dpA[i] = max(dpA[i-1] + A[i] - p , dpB[i-1] + A[i] )
        dpB[i] = max(dpB[i-1] + B[i] - p , dpA[i-1] + B[i] )


    print(f"#{tc+1} {max(dpA[N-1], dpB[N-1])}")











