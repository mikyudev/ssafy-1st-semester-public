import sys
sys.stdin = open("txt.txt")

# 종료조건
# 가지 수


# n 명의 모든 점원을 고려했을 때
# 가지치기 : 이미 b 이상 이면 쌓기 그만
# 가지의 수 :
# 점원을 탑에 포함시키는 경우 or 안 시키는 경우

def recur(idx, total_height):
    global min_answer
    if total_height >= B: # 가지치기: B 이상이면 더 이상
        min_answer = min(min_answer, total_height)
        return

    if idx == N:
        return

    recur(idx + 1, total_height + H[idx])  # 탑에 포함 시키는 경우
    recur(idx + 1, total_height)  # 탑에 포함 안 시키는 경우



T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = sorted(map(int, input().split()))
    min_answer = float('inf')  # 200000
    # min_answer = 21e8  # 이건 21억 임
    recur(0, 0)




    print(f"#{tc} {min_answer-B}")





#
# # b = 목표
# # n = 5명
# # h = 각 사람의 높이
#     statk = []
#     start = 0
#     for end in range(N):
#
#         while end < N:
#                 if H[start] + H[end] <= B:
#                     end += 1
#
#                 else:



