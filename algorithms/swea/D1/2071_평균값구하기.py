t = int(input())

for case in range(1, t+1):
    numbers = list(map(int,input().split()))
    avg_sum = 0 

    for n in numbers:
        if 0 <= n <= 10000:
            avg_sum = sum(numbers) / 10

    print(f"#{case} {round(avg_sum)}")





################## 밑은 완전 정답 코드 

t = int(input())

for case in range(1, t+1):
    numbers = list(map(int, input().split()))
    avg_sum = sum(numbers) / 10  # 10개의 수니까 그냥 나눠도 됨
    print(f"#{case} {round(avg_sum)}")
