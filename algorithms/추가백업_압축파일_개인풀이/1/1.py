# for문 이론 1
# n번 반복하는 반복문


 # 1번
# for i in range(9):
#     i = '#'
#     print(i, end='')

# for i in range(9):
#     print('#', end='')

# 2번
# for i in range(2):
#     for j in range(3):
#         print('#', end= '') # 별 3개 찍고
#     print() # 줄바꿈

# 3번
# n = int(input())
#
# for i in range(n):
#     print('#',end='')
# print()
# for j in range(n+5):
#     print('!',end='')


# 4번
# n = int(input())
#
# if n > 10:
#     for i in range(5):
#         print('#', end = '')
#
# else:
#     for i in range(n):
#         print('#',end='')


# 4번 오답

# n = int(input())
# for i in range(n):
#     if n > 10:
#         print('#'* 5)
#         n = 0
#     else:
#         print('#',end='')


# 5번
# for i in range(1,11):
#     print(i, end=' ')
# print()
# for j in range(10, 0, -1):
#     print(j, end=' ')


# 6번
# 암기요
# a , b = map(int,input().split())
# if a <= b:
#     for i in range(a, b+1):
#         print(i, end = ' ')
# else:
#     for j in range(a, b-1, -1):
#         print(j, end=' ')

# 파이널 1
# n = int(input())
##
# for i in range(n+1):
#     print(n+i, n + i + 1, n + i + 2)
#
# n = int(input())
# # 세로로 봤을 때 n의 두배까지
# for i in range(n, n*2+1):
#     # 가로로 봤을때 1씩 증가
#     print(i, i+1, i+2)
#



# 파이널 2

# n = int(input())
# num = 0
# if n % 2 == 0:
#     for _ in range(6):
#         print(n+num, end=' ')
#         num += 2
# else:
#     for j in range(11):
#         print(n+num, end=' ')
#         num += 3

#
# n = int(input())
#
# if n % 2 == 0: # 짝수인경우
#     for i in range(6):
#         print(n + 2 * i, end=' ')
# else:
#     for j in range(11):
#         print(n + 3 * j, end=' ')
#

# 반복문과 리스트
# 리스트(배열) : 여러개의 객체를 하나의 객체로 묶고싶다.

# 리스트 이론 1.
# sequence 자료형 (순서가 있다.) - 인덱싱, 슬라이싱, 순회,
# 가변자료형
# arr = [1, 2, 3, 4, 5]
# 1. 인덱싱 : 항상 0부터 시작
# 마지막 원소를 인덱싱 arr[-1], arr[len(arr) - 1]
# 2. 슬라이싱, 이 리스트를 거꾸로 슬라이싱
# arr[::-1]



# # 1번
# arr = [0] * 6
# arr[1] = 3
# arr[4] = 7
# arr[5] = 9
# print(arr[4]+arr[5])

#
# # 2번
# n = int(input())
# arr=[0] * 4
# arr[0] = n
# arr[1] = 3
# arr[2] = 2
# arr[3] = arr[1] + arr[2]
#
# print(*arr)

# 2 번 좋은 정답
# arr = [1, 3, 2, -5]  -> 하드코딩
#
# arr[0] = int(input())
# arr[3] = arr[1] + arr[2]
# print(*arr)


# 3번
# arr = [9, 5, 1, 15, 7, 3]
# for i in arr[::-1]:
#     print(i, end=' ')

# 순회하는 방식
# 1. iterator 방식
# # 2. indexing 방식 ↓↓↓↓↓↓↓↓↓
# arr = [9, 5, 1, 15, 7, 3]
# for i in range(len(arr)-1, -1, -1):
#     print(arr[i], end = ' ')
#




# 4 번 하기전에 이론 하나 ㅓ더 ~
# arr = [ 10, 10, 10, 10, 10, 10] 이렇게 채우고 싶다

# 첫 번째 방법  append
# arr = []
# for _ in range(6):
#     arr.append(10)


# 두 번째 방 법 인덱싱
# arr = [0] * 6
# for i in range(6):
#     arr[i] = 10

# 두 가지 방법 다 알고 있어야 함
# 4번

# arr = [0] * 8
# for i in range(4):
#     arr[i] = 7
# for j in range(4,8):
#     arr[j] = 15
# print(*arr)



# 파이널 1 번
# arr = []
# t = 10
# for _ in range(5):
#     arr.append(t)
#     t -= 3
# print(*arr)
######################################
# arr = []
# for i in range(10, -3, -3):
#     arr.append(i)

########################################

arr = []
# temp = 10
# for i in range(5)
#     arr.append(temp)
#     temp -= 3



# 파이널 2번

# arr = []
# a, b = map(int,input().split())
# for _ in range(3):
#     arr.append(a)
# for _ in range(2):
#     arr.append(b)
# for _ in range(3):
#     arr.append(a+b)
# print(*arr)




# 파이널 3 번
'''
arr = [2, 5, 1, 6, 4, 3]
total = 0
max_v = float('-inf')
min_v = float('inf')

for value in arr:
    total += value
print(total)

for i in arr:
    if max_v < i:
        max_v = i
        result = max_v
for j in arr:
    if min_v > j:
        min_v = j
        result = min_v

print(max_v - min_v)

'''


# sum_v = 0
# max_v = float('-inf')
# min_v = float('inf')
#
# arr = [2, 5, 1, 6, 4, 3]
#
# # iterator 방식
# for i in arr:
#     if i > max_v: max_v = i # 최대값 코드
#     if i < min_v: min_v = i # 최소값 코드
#     sum_v += i # 합계누적
#
# print(sum_v)
# print(max_v - min_v)




# O(nlogn) # O(logn) == 0(1) 비슷
# O(nlogn) == O(n) 비슷

# result = sorted(arr) # 원본 변경 x
# print(result)


# 버블정렬   =>  서술형에 나옴

arr = [12, 3, 9, 1, 15, 7]

# a = 리스트 (배열)
# N = 길이 (element 개수)
def bubble_sort(a, N):
    for i in range(N-1, 0, -1): # 범위의 끝 위치
        for j in range(i):   # 비교할 왼쪽 원소 인덱스 j # i-1까지 
            if a[j] > a[j+1]: # 왼쪽이 더 크면 자리교환 (핵심)
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(*bubble_sort(arr, len(arr)))



