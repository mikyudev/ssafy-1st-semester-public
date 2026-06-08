# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     # room = list(range(1, N))

#     cnt = N -1 
#     for i in range(1, N-1):
#         cnt += (i+1) - arr[i] +1 

#     print(f"#{tc} {cnt}")





# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [0] + list(map(int, input().split()))
#
#     i = 1
#     cnt = 0
#
#     while i < N:
#         if arr[i] == 0:
#             i += 1
#         else:
#             next_idx = arr[i]
#             arr[i] = 0
#             i = next_idx
#
#         cnt += 1
#
#     print(f"#{tc} {cnt}")




T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 5
    arr = list(map(int, input().split())) # 0 1 1 2 0

    i = 0
    cnt = 0

    while i < N-1:
        if arr[i] == 0:
            i += 1
        else:
            next_idx = arr[i] - 1   # 인덱스 1차이 조정
            arr[i] = 0
            i = next_idx
        cnt += 1

    print(f"#{tc} {cnt}")
