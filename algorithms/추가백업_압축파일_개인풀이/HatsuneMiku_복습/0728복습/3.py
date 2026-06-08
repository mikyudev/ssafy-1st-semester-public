# queue = [1, 2, 3]

# while True:
#     n = int(input())
    
#     for i in range(n):
#         front = queue.pop(0)
#         queue.append(front)

#     print(queue[0])
#     break




# arr = [2, 3, 4, 5, 1]
# while True:
#     n = int(input())

#     for i in range(n):
#         front = arr.pop(0)
#         arr.append(front)


#     print(arr[0])
#     break




queue = [1, 2, 3]
n = int(input())

# n 번 자리 바꾸기 
for _ in range(n):
        # 맨 앞의 친구를 뺀다
        front = queue.pop(0)
        # 맨 뒤에 추가 
        queue.append(front)

#맨 앞 친구 출력 
print(queue[0])
