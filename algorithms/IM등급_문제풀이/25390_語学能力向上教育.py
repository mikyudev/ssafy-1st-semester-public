T = int(input())
for tc in range(1, T+1):
    N, K_miku, teto = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    result = float('inf')

    for i in range(K_miku, N - (K_miku * 2) + 1):
        for j in range(i + K_miku, N - K_miku + 1):

            c = arr[:i]
            b = arr[i:j]
            a = arr[j:]

            if c[-1] == b[0]:
                continue
            if b[-1] == a[0]:
                continue

            if K_miku <= len(c) <= teto and K_miku <= len(b) <= teto and K_miku <= len(a) <= teto:
                arr1 = (len(c), len(b), len(a))
                result = min(result, max(arr1) - min(arr1))
remember

    if result == float('inf'):
        print(f"#{tc} -1")

    else:
        print(f"#{tc} {result}")
