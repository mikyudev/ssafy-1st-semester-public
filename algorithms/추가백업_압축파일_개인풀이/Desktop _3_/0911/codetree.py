N = int(input())

stack = []
for _ in range(N):
    num = int(input())
    stack.append(num)

max_v = max(stack)

cnt = 0
max_cnt = 0
for i in range(len(stack)):
    if stack[i] == max_v:
        cnt += 1

    else:
        cnt = 0

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)