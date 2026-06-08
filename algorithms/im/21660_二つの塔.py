T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int, input().split())
    cost = list(map(int, input().split()))

    cost.sort(reverse = True)
    種類 = list(range(1, M1+1)) + list(range(1, M2+1))
    種類.sort()
    # print(種類)


    result = 0
    for i, j in zip(cost, 種類):
        result += i * j

    print(f"#{tc} {result}")




