# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr1 = list(map(int, input().split()))
#     arr2 = list(map(int, input().split()))
#
#     # start, end 조건 써서 좌표 0 부터 돌리면서 최댓값 검사 하기
#
#     # ex)
#     # [0][0] [1][1] [2][2] sum
#     # [0][1] [1][2] [2][3] sum
#     # [0][2] [1][3] [2][4] sum
#     #
#     #               [2][5] stop
#     max_v = 0
#     sum = 0











T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # 어느 배열이 더 긴지, 짧은지 정해줍니다.
    # 코드를 일관성 있게 작성할 수 있습니다.
    if N > M:
        long_arr = arr1
        short_arr = arr2
    else:
        long_arr = arr2
        short_arr = arr1

    max_v = 0  # 최종 최댓값을 저장할 변수

    # 바깥쪽 루프: 짧은 배열이 움직일 시작 위치를 제어합니다.
    # (긴 배열 길이 - 짧은 배열 길이 + 1) 만큼 반복 가능합니다.
    for i in range(len(long_arr) - len(short_arr) + 1):

        current_sum = 0  # 현재 위치에서의 곱의 합을 저장할 변수

        # 안쪽 루프: 짧은 배열의 길이만큼 반복하며 마주보는 값들을 곱해서 더합니다.
        for j in range(len(short_arr)):
            # short_arr[j] 와 long_arr[i+j] 가 마주보게 됩니다.
            current_sum += short_arr[j] * long_arr[i + j]

        # 계산된 합(current_sum)이 지금까지의 최댓값(max_v)보다 크면,
        # 최댓값을 갱신합니다.
        if current_sum > max_v:
            max_v = current_sum

    print(f"#{tc} {max_v}")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # 어느 배열이 더 긴지, 짧은지 정해줍니다.
    # 코드를 일관성 있게 작성할 수 있습니다.
    if N > M:
        long_arr = arr1
        short_arr = arr2
    else:
        long_arr = arr2
        short_arr = arr1

    max_v = 0  # 최종 최댓값을 저장할 변수

    # 바깥쪽 루프: 짧은 배열이 움직일 시작 위치를 제어합니다.
    # (긴 배열 길이 - 짧은 배열 길이 + 1) 만큼 반복 가능합니다.
    for i in range(len(long_arr) - len(short_arr) + 1):

        current_sum = 0  # 현재 위치에서의 곱의 합을 저장할 변수

        # 안쪽 루프: 짧은 배열의 길이만큼 반복하며 마주보는 값들을 곱해서 더합니다.
        for j in range(len(short_arr)):
            # short_arr[j] 와 long_arr[i+j] 가 마주보게 됩니다.
            current_sum += short_arr[j] * long_arr[i + j]

        # 계산된 합(current_sum)이 지금까지의 최댓값(max_v)보다 크면,
        # 최댓값을 갱신합니다.
        if current_sum > max_v:
            max_v = current_sum

    print(f"#{tc} {max_v}")


## 밑은 똑같음




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if N > M:
        long_arr = arr1
        short_arr = arr2

    else:
        short_arr = arr2
        long_arr = arr1

    max_v = 0

    for i in range((len(long_arr)) - (len(short_arr)) +1):
        sum_v = 0
        for j in range(len(short_arr)):
            sum_v = long_arr[j] * short_arr[j+i]


    if max_v < sum_v:
        max_v = sum_v

print(f"#{tc} {max_v}")
