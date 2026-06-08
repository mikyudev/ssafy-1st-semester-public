import sys
sys.stdin = open('18541.txt')
#
# T =int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     # sample = list(map(int,input().split()))
#     # passcode = list(map(int, input().split()))
#     sample = input().split()
#     passcode = input().split()
#
#     sample = ''.join(sample)
#
#     start = 0
#     is_possible= 1
#
#     for char in passcode:
#         idx = sample.find(char, start)
#         if idx == -1:
#             is_possible = 0
#             break
#         else:
#             start = idx +1
#
#     print(f"#{tc} {is_possible}")














T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = input().split()
    passcode = input().split()

    sample = ''.join(sample)
    start = 0
    is_possible = 1

    for char in passcode:
        idx = sample.find(char,start)
        if idx == -1:
            is_possible = 0
            break

        else:
            start = idx+1

    print(f"#{tc} {is_possible}")




















