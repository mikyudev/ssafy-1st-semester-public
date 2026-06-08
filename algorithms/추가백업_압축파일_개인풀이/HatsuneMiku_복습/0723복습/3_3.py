cnt = 0

def factorial(n):
    # cnt = 0 문제점 : 재귀호출 할때마다 0으로 초기화
    global cnt # 전역변수 cnt를 수정 
    cnt += 1
    # 기저 조
    if n ==1:
        return 1
    else:
        return n * factorial(n-1) # 재귀호출
    
factorial(5)
print(cnt)






# cnt = 0
# def factorial(n):
#     global cnt
#     cnt += 1
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial)