from collections import deque


def bfs(start):
    q = deque()
    used = [0] * 6

    q.append(start)
    used[start] = 1

    while q:
        # 1. 큐에펏 뺸다 (탐색)
        now = q[0]
        print(chr(now + ord('A')), end=' ')
        q.popleft()

        for i in range(len(alist[now])):

            next = alist[now][i]
            # 이미 탐색했으면 continue
            if used[next] == 1: continue
            # 방문표시
            used[next] = 1
            q.append(next)  # 예약걸기
            # 방문기록 지우지 x


alist = [[] for _ in range(6)]
alist[0] = [1, 2]
alist[1] = [0, 2]
alist[2] = [0, 1, 3]
alist[3] = [2, 4]
alist[4] = [3]

n = int(input())
bfs(n)