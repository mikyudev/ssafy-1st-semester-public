# arr = list(map(int,input().split()))

# flag = 0
# for i in arr: 
#     if i % 2 == 0:
#         flag = 1
#         break

# # print(flag)


# arr = list(map(int,input().split()))

# for i in arr: 
#     if i % 2 == 0:
#         print(1)
#         break
# else:
#     print(0)

# is, get  붙여서 함수명  작성 굿 
def is_even(arr):
    for i in arr:
        if i % 2 == 0:
            return 1 # break 대신
        # for 문을 순회 했지만 return 1이 되지 않았따. 
    return 0


arr = list(map(int,input().split()))
result = is_even(arr)
print(result)


