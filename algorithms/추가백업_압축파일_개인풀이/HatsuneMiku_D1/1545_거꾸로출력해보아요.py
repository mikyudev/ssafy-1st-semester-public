# t = list(map(int,input().split()))

# for i in range(len(t)):
#     t[i] -= 1

# t.sort(reverse=True)
# print(*t)




# n = int(input())
# for i in range(n, -1, -1):  # n부터 0까지 1씩 감소
#     print(i, end=' ')



# # n = int(input())
# # t = list(range(n, -1, -1))
# # print(*t)



n = int(input())
t = list(range(n + 1))   # [0, 1, 2, ..., n]
t.sort(reverse=True)     # 거꾸로 정렬
print(*t)


# t = list(map(int, input().split()))
# t.sort(reverse=True)
# print(*t)
