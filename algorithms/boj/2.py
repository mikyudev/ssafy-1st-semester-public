# 카운팅 정렬 0805
# #
# def counting_sort(DATA, TEMP, k):
# # DATA [] -- 입력 배열(원소는 0이상 k이하 정수)
# # TEMP [] -- 정렬된 배열.
# # COUNTS [] -- 카운트 배열.

#     COUNTS = [0] * (k+1)

#     for i in range(len(DATA)): #DATA[i] 발생횟수 기록
#         COUNTS[DATA[i]] += 1

#     for i in range ( 1, k+1): # COUNT 값 조정 (누적)
#         COUNTS[i] += COUNTS[i-1]

#     for i in range(len(DATA)-1, -1, -1): # 3단계
#         COUNTS[DATA[i]] -= 1
#         TEMP[COUNTS[DATA[i]]] = DATA[i]


## Baby-gin Game



# 재밌넹 # 순열 PERMUTATION
# from itertools import permutations
# arr = [2, 3, 5, 7, 7, 7, 0, 0, 0, 0]
# nPr = list(permutations(arr, 10))
# for x in nPr:
#     print(x)
# print(len(nPr))
#
# 단순하게 순열을 생성하는 방법




# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1 :
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2 :
#                     print(i1, i2, i3)


# 탐욕 알고리즘



# # baby-gin
#
# num = 777567 # baby gin 으로 확인할 6자리 수
# c = [0] * 12 # 6자리 수로 각 자리 수를 추출하여 개수를 누적할 리스트
# for i in range(6):
#     c[num%10] += 1
#     num //= 10
# i = 0
# tri = run = 0
# while i < 10:
#     if c[i] >= 3: # triplete 조사 후 데이터 삭제
#         c[i] -= 3
#         tri+= 1
#         continue
#     if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사 후 데이터 삭제
#         c[i] -=1
#         c[i+1] -=1
#         c[i+2] -=1
#         run += 1
#         continue
#     i += 1
#
# if run + tri == 2: print("Baby Gin")
# else : print("Lose")




# n = int(input())
#
# for i in range(n):   # n 행
#     # print() 줄 바꿈 생겨서 여기 넣으면 오답임
#     for j in range(n):  # n 열
#         print('#', end='')
#     print()




# 2번 / 인덱싱 , 슬라이싱 두개 다 쓸 줄 알야함
# arr = ['A', 'B', 'Q', 'T']
#
# for i in range(4): # 4회 반복
#     for j in range(3, -1, -1):  # 역순 출력을
#         print(arr[j], end='')
#     print()



# 3번

# for y in range(4):  # 0, 1, 2, 3
#     for x in range(4): # 0을 4번 출력, 1을 4 번 출력
#         print(y, end='')
#     print()

# t = 0
# for y in range(4):
#     for x in range(4):
#         print(t, end='') # 0을 4번 출력, 1을 4번 출력
#     t += 1 # 아오 밖에 써야하네 .;
#     print()



# 4번
#
# for i in range(1, 4):   # y가 1인동안 x 는 1,2 ,3, 4  y가 2인 동안 ....
#     for j in range(1,5):
#         print(i, j)


########## 탐색 < ---> 완전 탐색
# 탐색: 내가 원하는 것을 찾는 것(특정 값, 조건을 만족하는)
#
# 완전탐색(브루트포스 알고리즘) : 모든 경우를 전부 확인하는 것
# 완전탐색 = 무조건 재귀로 풀어야함
#
#
# arr = [1, 4, 6, 1, 1, 9, 6]
# # q)탐색해서 1이 몇개인지 counting 해보기
# cnt = 0
# for a in arr: # iterator 방식 순회
#     if a == 1: cnt += 1
#
# print(cnt)




# 5번

# # a = list(map(int,input().split()))
# #
# # count = 0
# # for i in range(len(a)):
# #     if a[i] == 7:
# #         count+= 1
# print(count)

# arr = list(map(int,input().split()))
#
# count = 0
# for a in arr:
#     if a == 7: count+= 1
# print(count)





# # 2차원 리스트
# -----------------> x 좌표
# |
# |
# |
# |
# |
# |      arr[1][2]는 어디?
# y좌표  arr[y][x]
#         arr[행이 바뀐다][열이 바뀐다]




# 6번

# arr = [[0 for _ in range(4)] for _ in range(4)]
# arr = [[0] * 4 for _ in range(4)]
# #
# arr[0][0] = 7
# arr[1][3] = 1
# arr[2][1] = 3
# arr[3][3] = 9
# for row in arr:
#     print(*row)


# for a in arr:
#     print(*a)


# 7번
# arr = []
# for _ in range(4):
#     row = []
#     for _ in range(4):
#         row.append(0)
#     arr.append(row)

# arr = [[0 for _ in range(4)] for _ in range(4)]
# arr = [[0] * 4 for _ in range(4)]
# arr[0][0] = 7
# arr[1][3] = 1
# arr[2][1] = 3
# arr[3][3] = 9
# # print(*arr[-1])
# for x in range(4):
#     print(arr[3][x], end=' ')
#


# # 8번
# arr = [[7,1, 3, 5],
#         [9, 5, 9, 1],
#         [1, 3, 1, 5],
#         [3, 5, 9, 9]
#         ]
#
# print(arr[0][1])
# print(arr[1][2])
# print(arr[2][3])
# print(arr[3][0])






# # 9번  3번째 열 출력하기
# arr = [[7,1, 3, 5],
#         [9, 5, 9, 1],
#         [1, 3, 1, 5],
#         [3, 5, 9, 9]
#         ]
#
# for i in range(4):
#     print(arr[i][2], end=' ')


# for i in range(len(arr)):

# 00 10 20
# 01 11 21
# 02 12 22
# 03 13 23

# 열 순회 = y 순회

# 10번
# arr = [[5, 4, 2, 1],
#        [3, 7, 7, 7],
#        [2, 2, 1, 1]
#        ]
# # print(len(arr))
# for x in range(len(arr)+1):
#     for y in range(len(arr)):
#         print(arr[y][x], end = ' ')
#     print()

## 이론 !!!!!
# for y in range(4):
#     for x in range(4):
#         arr[y][x]   ### 이건 행 순회 !
# for x in range(4):
#     for y in range(4):
#         arr[x][y]   ### 이건 열 순회 !






# 11 번
'''
t = int(input())
# a = list(map(int,input().split()))
# arr = [[0] * 4 for _ in range(4)]

arr[]
for arr in range(t):
    a = list(map(int, input().split()))

    print(arr)        
# '''
#여기는 오답




# 방법 1
# arr = [list(map(int,input().split())) for _ in range(4)]
# 방법 2
# arr = []
# for _ in range(4):
#     a = list(map(int, input().split()))
#     arr.append(a)

# arr = [list(map(int, input().split())) for _ in range(4)]
# for row in arr[::-1]:
#     print(*row[::-1])
#
# arr = [list(map(int, input().split())) for _ in range(4)]
# for y in range(3, -1, -1):  # 3부터 0까지 1씩 감소
#     for x in range(3, -1, -1): # 3부터 0까지 1씩 감소
#         print(arr[y][x], end = ' ')
#     print()




# 파이널 !!
#
# arr = [list(map(int,input().split())) for _ in range(5)]
# cnt = 0
# max_v = float('-inf')
# min_v = float('inf')
# sum_v = 0


# # 행순회
# for y in range(5):
#     for x in range(5):
#         if arr[y][x] == 2: cnt += 1
#             # 최대값 코드
#         if arr[y][x] > max_v: max_v = arr[y][x]
#          # 최소값 코드
#         if arr[y][x] < min_v: min_v = arr[y][x]
#
#
#     sum_v += arr[y][y] # 00 11 22 33 44
# print(cnt)
# print(max_v, min_v)
# print(sum_v)
#




#
# arr = [list(map(int,input().split())) for _ in range(5)]
# cnt = 0
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == 2:
#             cnt += 1
# print(cnt)
# #
# max_v = 0
# min_v = 0
# for i in range(5):
#     for j in range(5):
#         max_v = max(arr[i][j])
#         min_v = min(arr[i][j])
# print(f"{max_v} {min_v}")

# for i in range(5):
# for j in range(5):
#
#
#
# 00 11 22 33 44


############ 카운팅 정렬
'''
DAT 자료구조

DAT : 값을 인덱스로 쓰는 자료구조
arr = [2, 1, 4, 4, 2, 2, 1, 1]
DAT = [0] * (4+1)     # 가장큰값 +1
DAT = [0, 0, 0, 0, 0]
     # 0  1  2  3  4  개수
DAT = [0, 2, 3, 0, 2]
'''

# arr = [2, 1, 4, 4, 2, 2, 1, 1]
#
# dat = [0] * 5
# idx = 0
#
# for i in range(len(arr)):
#     idx = arr[i] # 값을
#     dat[idx] += 1 # 인덱스로 쓴다 (카운팅)
#
# for i in range(len(dat)): # 0, 1, 2, 3, 4 만 반복
#     if dat[i] > 0: print(f"{i} : {dat[i]}")
#
# # dat 자료구조를 확실히 알아야 카운팅정렬 이해 쉬움





def counting_sort(DATA, TEMP, k):

# DATA [] -- 입력 배열 (원소는 0 이상 k이하 정수)
# TEMP [] -- 정렬된 배열
# COUNTS [] -- 카운트 배열

    COUNTS = [0] * (k+1)

    for i in range(len(DATA)) : # DATA[i] 발생횟수 기록
        COUNTS[DATA[i]] += 1

    for i in range(1, k+1) : # COUNTS 값 조정 (누적)
        COUNTS[i] += COUNTS[i-1]

    for i in range(len(DATA)-1, -1, -1): # 3단계
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]

    return TEMP


arr = [12, 3, 9, 1, 15, 7]
sorted_arr = sorted(arr)
# print(sorted_arr)

print(*counting_sort(arr,sorted_arr, 15 ))


# def counting_sort(DATA, TEMP, k):
#
# # DATA [] -- 입력 배열 (원소는 0 이상 k이하 정수)
# # TEMP [] -- 정렬된 배열
# # COUNTS [] -- 카운트 배열
#
#     COUNTS = [0] * (k+1)
#
#     for i in range(len(DATA)) : # DATA[i] 발생횟수 기록
#         COUNTS[DATA[i]] += 1
#
#     for i in range(1, k+1) : # COUNTS 값 조정 (누적)
#         COUNTS[i] += COUNTS[i-1]
#
#     for i in range(len(DATA)-1, -1, -1): # 3단계
#         COUNTS[DATA[i]] -= 1
#         TEMP[COUNTS[DATA[i]]] = DATA[i]
#
#     return TEMP
#
#
# arr = [12, 3, 9, 1, 15, 7]
# sorted_arr = sorted(arr)
# # print(sorted_arr)
#
# print(*counting_sort(arr,sorted_arr, 15 ))



def counting_sort(result):
    dat = [0] * (k + 1)
    # 1단계 counting
    for i in range(len(arr)):
        dat[arr[i]] += 1
    # 2단계 dat값 조정(누적)
    for i in range(1, k + 1):
        dat[i] += dat[i-1]
    # 3단계 뒤에서부터 정렬된 배열 생성
    for i in range(len(arr)-1, -1, -1):
        dat[arr[i]] -= 1
        # temp = dat[arr[i]]
        result[dat[arr[i]]] = arr[i] # 0으로 채워져 있어야 인덱싱 가능
        # 지역변수

arr = [12, 3, 9, 1, 15, 7]
k = 15
result = [0] * len(arr)
# global 쓰던지 아니면 매개변수로 들어가던지
# 지역변수로 바껴야 함

# 함수호출
counting_sort(result)

print(*result)


# 디버깅
# 1. 중단점(breaking point) 찍기
#   : 함수호출하는 부분, 내가 세세히 알고싶은 부분

# 2. Debug 'main' = 단축키 'f5'

# 3. step into는 함수 안으로 들어가기 'f11'
#    step over는 다음단계 진행  'f10'
