T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    最初 = [0] * N


    cnt = 0
    for i in range(N):
        # if arr[i] != 最初[i]:
        if 最初[i] != arr[i]:
            cnt += 1
            for j in range(i, N, i+1):
                if 最初[j] == 1:
                    最初[j] = 0
                else:
                    最初[j] = 1

    print(f"#{tc} {cnt}")
