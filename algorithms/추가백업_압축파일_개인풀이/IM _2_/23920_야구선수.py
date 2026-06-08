import sys
sys.stdin = open('23920.txt')

# end - start 가 k보다 작거나 같으면 된다


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))


    arr.sort()

    start = 0
    # cnt = 0
    max_v = 0
    for end in range(len(arr)):
        if arr[end] - arr[start] <= K:
            cnt = end - start +1
            # cnt += 1
        else:
            start +=1


        if max_v < cnt:
            max_v = cnt
    print(f"#{tc} {max_v}")