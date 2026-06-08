# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     total = n -1
#     for i in range(1, n-1):
#         total += (i+1 - arr[i]) + 1
#
#     print(f"#{tc} {total}")


#
#
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
#             i +=1
#
#         else:
#             next_idx = arr[i]
#             arr[i] = 0
#             i = next_idx
#
#         cnt +=1
#
#     print(f"#{tc} {cnt}")
#
#



T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    result = float('inf')

    for i in range(M, N - (2*M) +1):
        for j in range(i+M, N - M +1):

            C = arr[:i]
            B = arr[i:j]
            A = arr[j:]


            if C[-1] == B[0]:
                continue
            if B[-1]== A[0]:
                continue


            if M<=len(C)<=K and M<=len(B)<=K and M<=len(A)<=K:
                # print(f"{A} {B} {C}")
                diff = max(len(C), len(B), len(A)) - min(len(C), len(B), len(A))
                result = min(result, diff)




    if result == float('inf'):
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {result}")





