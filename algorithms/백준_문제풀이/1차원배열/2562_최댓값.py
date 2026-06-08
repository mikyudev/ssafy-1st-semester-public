
max_v = float('-inf') 
max_idx = 0
for i in range(9):
    a = int(input())
    if max_v < a:
        max_v = a
        max_idx = i
print(max_v)
print(max_idx + 1 )



# nums = [int(input()) for _ in range(9)]
# print(max(nums))
# print(nums.index(max(nums)) + 1)
