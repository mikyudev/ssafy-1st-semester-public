
text= "Python"

print(text[-1:2:])


# for臾??대줎 1
# n踰?諛섎났?섎뒗 諛섎났臾?


 # 1踰?
# for i in range(9):
#     i = '#'
#     print(i, end='')

# for i in range(9):
#     print('#', end='')

# 2踰?
# for i in range(2):
#     for j in range(3):
#         print('#', end= '') # 蹂?3媛?李띻퀬
#     print() # 以꾨컮轅?

# 3踰?
# n = int(input())
#
# for i in range(n):
#     print('#',end='')
# print()
# for j in range(n+5):
#     print('!',end='')


# 4踰?
# n = int(input())
#
# if n > 10:
#     for i in range(5):
#         print('#', end = '')
#
# else:
#     for i in range(n):
#         print('#',end='')


# 4踰??ㅻ떟

# n = int(input())
# for i in range(n):
#     if n > 10:
#         print('#'* 5)
#         n = 0
#     else:
#         print('#',end='')


# 5踰?
# for i in range(1,11):
#     print(i, end=' ')
# print()
# for j in range(10, 0, -1):
#     print(j, end=' ')


# 6踰?
# ?붽린??
# a , b = map(int,input().split())
# if a <= b:
#     for i in range(a, b+1):
#         print(i, end = ' ')
# else:
#     for j in range(a, b-1, -1):
#         print(j, end=' ')

# ?뚯씠??1
# n = int(input())
##
# for i in range(n+1):
#     print(n+i, n + i + 1, n + i + 2)
#
# n = int(input())
# # ?몃줈濡?遊ㅼ쓣 ??n???먮같源뚯?
# for i in range(n, n*2+1):
#     # 媛濡쒕줈 遊ㅼ쓣??1??利앷?
#     print(i, i+1, i+2)
#



# ?뚯씠??2

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
# if n % 2 == 0: # 吏앹닔?멸꼍??
#     for i in range(6):
#         print(n + 2 * i, end=' ')
# else:
#     for j in range(11):
#         print(n + 3 * j, end=' ')
#

# 諛섎났臾멸낵 由ъ뒪??
# 由ъ뒪??諛곗뿴) : ?щ윭媛쒖쓽 媛앹껜瑜??섎굹??媛앹껜濡?臾띔퀬?띕떎.

# 由ъ뒪???대줎 1.
# sequence ?먮즺??(?쒖꽌媛 ?덈떎.) - ?몃뜳?? ?щ씪?댁떛, ?쒗쉶,
# 媛蹂?먮즺??
# arr = [1, 2, 3, 4, 5]
# 1. ?몃뜳??: ??긽 0遺???쒖옉
# 留덉?留??먯냼瑜??몃뜳??arr[-1], arr[len(arr) - 1]
# 2. ?щ씪?댁떛, ??由ъ뒪?몃? 嫄곌씀濡??щ씪?댁떛
# arr[::-1]



# # 1踰?
# arr = [0] * 6
# arr[1] = 3
# arr[4] = 7
# arr[5] = 9
# print(arr[4]+arr[5])

#
# # 2踰?
# n = int(input())
# arr=[0] * 4
# arr[0] = n
# arr[1] = 3
# arr[2] = 2
# arr[3] = arr[1] + arr[2]
#
# print(*arr)

# 2 踰?醫뗭? ?뺣떟
# arr = [1, 3, 2, -5]  -> ?섎뱶肄붾뵫
#
# arr[0] = int(input())
# arr[3] = arr[1] + arr[2]
# print(*arr)


# 3踰?
# arr = [9, 5, 1, 15, 7, 3]
# for i in arr[::-1]:
#     print(i, end=' ')

# ?쒗쉶?섎뒗 諛⑹떇
# 1. iterator 諛⑹떇
# # 2. indexing 諛⑹떇 ?볛넃?볛넃?볛넃?볛넃??
# arr = [9, 5, 1, 15, 7, 3]
# for i in range(len(arr)-1, -1, -1):
#     print(arr[i], end = ' ')
#




# 4 踰??섍린?꾩뿉 ?대줎 ?섎굹 ?볥뜑 ~
# arr = [ 10, 10, 10, 10, 10, 10] ?대젃寃?梨꾩슦怨??띕떎

# 泥?踰덉㎏ 諛⑸쾿  append
# arr = []
# for _ in range(6):
#     arr.append(10)


# ??踰덉㎏ 諛?踰??몃뜳??
# arr = [0] * 6
# for i in range(6):
#     arr[i] = 10

# ??媛吏 諛⑸쾿 ???뚭퀬 ?덉뼱????
# 4踰?

# arr = [0] * 8
# for i in range(4):
#     arr[i] = 7
# for j in range(4,8):
#     arr[j] = 15
# print(*arr)



# ?뚯씠??1 踰?
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



# ?뚯씠??2踰?

# arr = []
# a, b = map(int,input().split())
# for _ in range(3):
#     arr.append(a)
# for _ in range(2):
#     arr.append(b)
# for _ in range(3):
#     arr.append(a+b)
# print(*arr)




# ?뚯씠??3 踰?
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
# # iterator 諛⑹떇
# for i in arr:
#     if i > max_v: max_v = i # 理쒕?媛?肄붾뱶
#     if i < min_v: min_v = i # 理쒖냼媛?肄붾뱶
#     sum_v += i # ?⑷퀎?꾩쟻
#
# print(sum_v)
# print(max_v - min_v)




# O(nlogn) # O(logn) == 0(1) 鍮꾩듂
# O(nlogn) == O(n) 鍮꾩듂

# result = sorted(arr) # ?먮낯 蹂寃?x
# print(result)


# Bubble sort

arr = [12, 3, 9, 1, 15, 7]

# a = 由ъ뒪??(諛곗뿴)
# N = 湲몄씠 (element 媛쒖닔)
def bubble_sort(a, N):
    for i in range(N-1, 0, -1): # 踰붿쐞?????꾩튂
        for j in range(i):   # 鍮꾧탳???쇱そ ?먯냼 ?몃뜳??j # i-1源뚯? 
            if a[j] > a[j+1]: # ?쇱そ?????щ㈃ ?먮━援먰솚 (?듭떖)
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(*bubble_sort(arr, len(arr)))






