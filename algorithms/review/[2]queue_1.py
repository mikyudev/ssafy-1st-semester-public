##############################################################################################
# O(n)   = pop(0)

# O(1)   = popleft()  / deque = 양쪽 끝 연산 최적화 자료구조
##############################################################################################


from collections import deque


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split())) # 5527 731 31274

    queue = deque(arr)  # 731 31274 5527

    for _ in range(M):
        item = queue.popleft() # 앞에 하나 뽑아서 item  에 넣어삐서

        queue.append(item)  # 그거 뒤에 추가예~ 


    print(f"#{tc} {queue.popleft()}")


##############################################################################################
# 화덕 피자
##############################################################################################

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    pizzas = deque([i + 1, p] for i ,p in enumerate(cheese))


    oven = deque()
    for _ in range(N):
        if pizzas:
            oven.append(pizzas.popleft())

    while len(oven) > 1:
        now = oven.popleft()
        now[1] //=2
        if now[1] == 0:
            if pizzas:
                oven.append(pizzas.popleft())
        else:
            oven.append(now)


    print(f"#{tc} {oven[0][0]}")