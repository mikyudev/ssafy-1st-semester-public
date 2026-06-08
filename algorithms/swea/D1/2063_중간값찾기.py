t = int(input())
numbers = list(map(int,input().split()))

numbers.sort()
mid = t // 2 

print(numbers[mid])






# 중간값 함수 

#     a.sort()
#     b = len(a)
#     mid = n // 2

#     if n % 2 ==1:
#         return a[mid]
#     else:
#         return a[mid-1]+a[mid] / 2 