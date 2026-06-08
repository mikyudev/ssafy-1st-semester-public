T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = input().split()
    passcode = input().split()

    sample = ''.join(sample)
    # print(sample)


    start = 0
    is_possible = 1
    for num in passcode:
        idx = sample.find(num, start)
        if idx == -1:
            is_possible = 0
            break
        else:
            start = idx + 1

    print(f"#{tc} {is_possible}")
