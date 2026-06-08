# n = int(input())

# a = list(map(int,input().split()))

# # max_v = float('-inf')
# # min_v = float('inf')
# max_v = 0
# min_v = 0
# for i in range(n):
#     max_v = max(a)
#     min_v = min(a)
# print(f"{min_v} {max_v}")




# max , min 안 쓰고 


n = int(input())
a = list(map(int,input().split()))


max_v = float('-inf')
min_v = float('inf')

for i in range(n):
    if max_v < a[i]:
        max_v = a[i]
        result = max_v
    if min_v > a[i]:
        min_v = a[i]
        result = min_v
print(f"{min_v} {max_v}")