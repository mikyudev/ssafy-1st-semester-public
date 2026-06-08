t = int(input())

for case in range(1, t+1):
    numbers = list(map(int,input().split()))

    if numbers[0] < numbers[1]:
        print(f"#{case} <")

    elif numbers[0] == numbers[1]:
        print(f"#{case} =")

    else:
        print(f"#{case} >")