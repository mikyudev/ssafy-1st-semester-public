import sys
sys.stdin = open("2819.txt")

# 상하좌우 델타배열

# visited 안 쓴다

# 서로 다른 수 set

# 6번 이동


# 1. 종료조건 : 6번
# 2. 가지의 수 : 4개 (상하좌우)


# 재귀호출 안 할래 => queue





dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 1. 종료조건 : 숫자 7자리 일 때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(y, x, number):
    if len(number) == 7:
        result.add(number)
        return

    for i in range(4): # 상하좌우
        ny = y + dy[i]
        nx = x + dx[i]
        # 범위 밖이면 다음
        if ny < 0 or nx < 0 or ny >= len(matrix) or nx >=len(matrix): continue

        # if visited[ny][nx]:continue 이런거 필요 x 중복 가능임
        recur(ny, nx, number + matrix[ny][nx])


T = int(input())

for tc in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    # print(matrix)
    result = set()

    # 7자리 만드는 코드
    # 모든 점이 출발점 가능
    for sy in range(len(matrix)):
        for sx in range(len(matrix)):
            recur(sy,sx, matrix[sy][sx])

    print(result)
    print(f"#{tc} {len(result)}")


