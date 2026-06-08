
T = int(input())

arr = [[0] * 100 for _ in range(100)]

sum_v = 0
for tc in range(T):
    x, y = map(int,input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                sum_v += arr[i][j]

print(sum_v)
            

# T = int(input())

# arr = [[0] * 100 for _ in range(100)]

# sum_v = set()
# for tc in range(T):
#     x, y = map(int,input().split())
#     for i in range(y, y+10):
#         for j in range(x, x+10):
#                 sum_v.add((i,j))

# print(len(sum_v))
            


         

# import sys
# input = sys.stdin.readline

# N = int(input())                         # 색종이 수
# paper = [[0]*100 for _ in range(100)]    # 100x100 도화지

# for _ in range(N):
#     x, y = map(int, input().split())     # 왼쪽 변, 아래쪽 변과의 거리 (0~90)
#     for i in range(y, y+10):             # y는 행(아래->위), i: 0~99
#         for j in range(x, x+10):         # x는 열(왼->오), j: 0~99
#             paper[i][j] = 1              # 겹치면 그대로 1

# # 검은 영역 넓이 = 1의 개수
# print(sum(map(sum, paper)))



