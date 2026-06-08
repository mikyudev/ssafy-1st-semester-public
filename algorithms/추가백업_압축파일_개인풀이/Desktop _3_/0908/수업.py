# 종료조건 : 3먕을 모두 고려하면 종료
# 가지수 (후보수) : 2개 (o, x )

#############################################################################
# 3명의 친구 부분집합 찾기
#############################################################################

# arr = ['O', 'X']
# name = [ 'MIKU', 'HAKU', 'TETO']
#
# path = []
#
# def recur(cnt):
#     # 종료조건 (3명을 모두 고려)
#     if cnt == 3:
#         print(*path)
#         return
#
#
#     # 재귀호출 파트
#     # - 부분집합에 포함되는 경우 (O를 추가)
#     path.append(arr[0])
#     recur(cnt + 1)
#     path.pop()
#
#
#     # - 포함되지 않는 경우 (X를 추가)
#     path.append(arr[1])
#     recur(cnt + 1 )
#     path.pop()
#
# recur(0)  # 0명을 고려한 상태로 시작
#
#
# def recur(cnt, path):
#
#     if cnt == 3:
#         print(*path)
#         return
#     # 부분집합에 포함 시키는 경우
#     recur(cnt + 1, path + [name[cnt]])
#     # 포함시키지 않는 경우
#     recur(cnt + 1, path)
#
# name = [ 'MIKU', 'HAKU', 'TETO']
# recur(0, [])
#
#
#
#
#
# #############################################################################
# # 바이너리 카운팅
# #############################################################################
#
# #
# arr = [1, 2, 3, 4]
#
# # i = 0~2^n == i번째 부분집합
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         if i & (1 <<idx):
#             print(arr[idx], end = " ")
#
#     print()
#
#
#
#
# # 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크하는 코드
# arr = ['A', 'B', 'C' ]
# n = len(arr)
# def get_sub(tar):
#     print()
#     print(f'target = {tar}', end=' / ')
#     for i in range(n):
#         if tar & 0x1: # 가장 우측 비트를 체크  # 0x1(16진수 1), 0b1(2진수 1), 1, 0b0001, True 다 됨
#             # 0x1로 표기한 이유 = 비트 연산임을 명시하는 권장 방법 (암묵적 룰)
#             print(arr[i], end=' ')
#         tar >>= 1
#
# for t in range(1<<n):
#     get_sub(t)


################################################################
# 순열
##############################################################


# arr = ['A', 'B', 'C', 'D', 'E']
# N = 3
# path = []
#
# def recur(cnt):
#     # N명을 뽑으면 종료
#     if cnt == N:
#         print(*path)
#         return
#
#     for i in range(len(arr)):
#         path.append(arr[i])
#         recur(cnt + 1 )
#         path.pop()
#
#
# recur(0)

#
# arr = ['A', 'B', 'C', 'D', 'E']
# N = 3
# path = []
#
# def recur(cnt, start):
#     # N명을 뽑으면 종료
#     if cnt == N:
#         print(*path)
#         return
#
#     for i in range(start, len(arr)):
#         path.append(arr[i])
#         # recur(cnt + 1, i) # i 번쨰를 골랐으니, 다음 선택은 i 부터 고려 (중복을 허용하는 조합)
#         recur(cnt + 1, i+1) # i 번쨰를 골랐으니, 다음 선택은 i+1 부터 고려 (중복을 허용하지 않는 조합)
#         path.pop()
#
#
# recur(0, 0)




################################################################
# 그리디 ( 현재 기준으로 가장 좋아 보이는 선택지로 결정 -> 답 도출)
################################################################

# 1. 규칙성을 찾아야 한다.


# 동전교환문제


n=1730
arr = [10, 50, 100, 500]
arr.sort(reverse=True)
cnt = 0
# Greedy 문제의 단골 손님
# 정렬 연습 : 튜플이라면 ? 인스턴스 리스트? 역순이라면?
#     예) 길이가 우선 정렬, 같은 길이는 사전 순으로 정렬
# list.sort() vs sorted() !!!!!!

for i in arr:
    a= n // i
    cnt += a
    n = n % i



print(cnt)




# 화장실

arr = [15 ,30, 50, 10]
n = len(arr)-1

arr.sort()
total = 0
for time in arr:
    total += time * n
    n -= 1

print(total)


# 회의실 배정문제
# 종료시간 기준으로 sort 하기
stack = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    stack.append([a, b])

    stack.sort(key=lambda x: x[1])

# 종료시간 기준으로 이제 최대 회의 개수






## 순조부, 문제들의 접근법

## 그리디 규칙을 잘 찾고, 조건 검증, 많은 문제 풀어봐야함.