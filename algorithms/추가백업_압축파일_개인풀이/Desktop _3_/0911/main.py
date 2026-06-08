# N - Queen


def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가?
    for y in range(row):
        if visited[y][col]:
            return False

    # 2. 좌상단 대각선에 놓은 적이 있는가?　
    y,x = row -1, col -1
    while y >= 0 and x >= 0:
        if visited[y][x]:
            return False
        y -= 1
        x -= 1

        # [참고] for 문으로 하고싶다!
    # for y, x in zip(range(row -1, -1, -1), range(col-1, -1, -1)):
    #     if visited[y][x]:
    #         return False

    # 3. 우상단 대각선에 놓은 적이 있는가? (/)
    y, x = row - 1, col + 1
    while y >= 0 and x < N:
        if visited[y][x]:
            return False
        y -= 1
        x += 1
    return True


# 종료 조건 : N 개의 행을 모두 고려하면 종료
# 가지의 수 : N 개의 열
def recur(row):
    global answer
    if row == N:
        answer +=1
        # print(*path)
        return
    for col in range(N):
        # 가지치기 : 같은 열을 못 고르도록
        # --> 유망하지 않은 케이스를 모두 삭제 ( 세로, 대각선 )
        if check(row, col) is False:
            continue # 체크했는데 false면 걍 넘어가라 이런 거 구조 잡고 시작해야함

        visited[row][col] = 1
        # col을 선택했다
        path.append(col)
        recur(row + 1)
        path.pop()
        visited[row][col] = 0


N = int(input())
visited = [[0] * N for _ in range(N)]
answer = 0 # 가능한 정답 수
path = [] # 임시변수 (경로출력을 위해 )
recur(0)

print(f'{answer}')



N = 8
visited = [[0] * N for _ in range(N)]
answer = 0 # 가능한 정답 수
path = [] # 임시변수 (경로출력을 위해 )
recur(0)

print(f' N={N} / answer = {answer}')



################################################################################################
################################################################################################

# print(ord(input()))

# n = int(input())
# s = input()
# sum_v = 0
# for i in range(n):
#     sum_v += int(s[i])
#
# print(sum_v)

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', "t", 'u', 'v', 'w', 's', 'x', 'y', 'z']
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#
# alpha = []
# for i in range(ord('a'), ord('z') +1):
#     alpha.append(chr(i))
#
# n = input()
# for i in alpha:
#     b = n.find(i)
#     print(b, end = ' ')


# T = int(input())
# for _ in range(T):
#     a, b = input().split()
#     a = int(a)
#     # b =str(b)
#
#     for c in b:
#         print(c * a, end ='')
#     print()
#
#


# n = input()
# stack = []
# for i in n.split():
#     stack.append(i)
#
# print(len(stack))


# a, b = input().split()
#
#
# a = int(a[::-1])
# b = int(''.join(reversed(b)))
#
#
# print(max(a, b))
# print(a+ b)

#
# a, b = input().split()
#
# a = a[::-1]
# b = ''.join(reversed(b))
#
# print(max(a, b))
# print(a+b)

# n = input()
# total = 0
#
# # list= [1, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ','0']
#
# alpha=[]
# for i in range(ord('A'), ord('Z')+1):
#     alpha.append(chr(i))
#
# for j in n:
#     d = alpha.index(j)
#     if 0 <= d <=2:
#         total +=3
#     elif 3 <= d <=5:
#         total += 4
#     elif 6 <= d <=8:
#         total += 5
#     elif 9 <= d <=11:
#         total += 6
#     elif 12 <= d <=14:
#         total += 7
#     elif 15 <= d <=18:
#         total += 8
#     elif 19 <= d <=21:
#         total += 9
#     elif 22 <= d <=25:
#         total += 10
#     elif j == '1':
#         total += 2
#
#     elif j == '0':
#         total += 11
#
# print(total)


# a = input().strip()
# b = input().strip()
# c = input().strip()
#
# print(a)
# print(b)
# print(c)


# while True:
#     try:
#         print(input())
#     except:
#         break
#
#
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")




# 1. 슬라이딩 윈도우  윈도우 swea 올라와있음
# 2. 순열 (순열 used배열)  + 백트래킹 swea에 올라와있음
# 3. 서술형
# 어떤 명제를 증명하는데에 있어서 참인걸
# 대우 명제가 참이면 원래 명제가 참





# 1. 슬라이딩 윈도우      40
    # 윈도우 어쩌고 저쩌고 하면서 나옴




# 2. 순열(used배열) + 백트래킹  35 점
    # 순조부!







# 3. 서술형 25점

# 3-1. 3n + 5 가 홀수이면 n 은 짝수이다  !!! 증명하시오 !!!

# 대우
# p이면 q이다  = >  ~q이면 ~p이다
# n이 홀수면 3n+5는 짝수다

# 홀수면 n = 2k +1
# 3n + 5 = 3(2k+1) + 5 = 6k + 8 = 2(3k+4) 로 짝수 (2의 배수니까 )

# 대우가 참이므로 원 명제도 참이다  (대우명제를 보여주면서 증명할 수 있음)





# 3-2
# T(n) = T(n-1) + 1, T(0) = 1
# T(n-1) = T(n-2) + 1
# T(n) = T(n-2) + 2   = T(n-k) + k     k = n 이라고 가정하면
#        = T(0) + n = n +1

# O(T(n)) = O(n+1) = O(n)

