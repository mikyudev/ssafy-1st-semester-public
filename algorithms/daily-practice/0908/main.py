T, M = map(int, input().split())


my_list = list(range(1, T+1))

for _ in range(M):
    a, b = map(int, input().split())
    my_list[a], my_list[b] = my_list[b], my_list[a]


print(*my_list)



# 종료조건 : 3먕을 모두 고려하면 종료
# 가지수 (후보수) : 2개 (o, x )