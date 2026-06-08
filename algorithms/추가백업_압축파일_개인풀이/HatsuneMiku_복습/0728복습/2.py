stack = [] 

while True:
    n = int(input())
    # 0이 입력되면 append하지 않고 break먼저 
    if n == 0:
        break
    stack.append(n) # 스택에 추가 

word = '' 
while stack: # stack 이 빌때까지 반복
    word += str(stack.pop()) # 후입선출 --> 역순으로 
print(word)
    











# stack = [] 

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     stack.append(n)

# result = ''
# while stack:
#     result = str(stack.pop())
#     print(result)
