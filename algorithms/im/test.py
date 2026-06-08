T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = N / 2

    arr.sort()


    result = float('inf')

    for i in range(1, N-2+1):
        for j in range(i+1, N):

            c = arr[:i]
            b = arr[i:j]
            a = arr[j:]


            if c[-1] == b[0]:
                continue

            if b[-1] == a[0]:
                continue


            if 1<=len(c)<=max_v and 1<=len(b)<=max_v and 1<=len(a)<=max_v:
                max_len = max(len(c), len(b), len(a))
                min_len = min(len(c), len(b), len(a))
                result1 = max_len - min_len
                if result > result1:
                    result = result1


    if result == float('inf'):
        print(f"#{tc} -1")

    else:
        print(f"#{tc} {result}")





