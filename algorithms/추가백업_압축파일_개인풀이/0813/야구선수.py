

# 이 문제의 핵심도 바로 슬라이딩 윈도우(Sliding Window) 또는 투 포인터(Two Pointers) 기법입니다.
# 정렬된 배열 위를 start와 end라는 두 개의 포인터가 미끄러지듯 움직이며 조건을 만족하는 가장 긴 구간을 찾는 방식이죠.



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    # 슬라이딩 윈도우!!!! 변수 !! 준비!
    start = 0
    max_sixe = 0


    # end 포인터를 오른쪽으로 이동시키면서 창문을 넓혀
    # for end in range(N):
    #
    #
    #     while arr[end] - arr[start] > M:
    #         start +=1
    #
    #     current = end - start + 1
    #
    #     if max_sixe < current:
    #         max_sixe = current
    #
    # print(f"#{tc} {max_sixe}")




    # 최대 최소의 차가 m보다 작으면 모두가 합격


        # if arr[-1] - arr[0] <= M:
        #     print(len(arr))
        #
        # if arr[i] - arr[i+1]