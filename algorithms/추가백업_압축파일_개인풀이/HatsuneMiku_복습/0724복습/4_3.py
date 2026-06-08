# my_list = [0, 0, 0, 0, 0]

# for i in range(len(my_list)):
#     my_list[i] += i + 5 

# print(*my_list)


arr = [0] *5 

for i in range(5):
    arr[i] = i + 5

for num in arr:# iterator 방식 순회 
    print(num, end = ' ')