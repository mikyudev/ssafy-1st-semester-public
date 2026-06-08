T = int(input())

count = 0
for _ in range(T):
    a, b = map(int,input().split())
    count += 1
    print(f"Case #{count}: {a+b}")