H, M = map(int,input().split())
T = int(input())

if M + T <= 59:
    M = M + T

elif M + T == 60:
    M = 0
    H += 1
    if H > 23:
        H = 0

# else:
#     M = M + T - 60 
#     H += 1
#     if M == 60:
#         M = 0 
#         H += 1 
#     else:
#         H = 0

else:
    M = M + T
    H += M // 60       # 넘치는 분만큼 시간 증가
    M = M % 60         # 분 정리

    if H > 23:
        H = H % 24 


###############################################################################

print(H , M)

H > 23

H, M = map(int, input().split())
T = int(input())

M += T
H += M // 60
M %= 60
H %= 24

print(H, M)

##################################################################################

H, M = map(int, input().split())
T = int(input())

# 분 먼저 더하기
M += T

# 60분을 초과하면 시간으로 넘기기
if M >= 60:
    H += M // 60    # 넘기는 시간 더하기
    M = M % 60      # 남는 분 계산

# 시간이 24를 넘으면 다시 0부터 시작
if H > 23:
    H = H % 24

print(H, M)
