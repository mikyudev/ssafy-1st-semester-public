# 특정 구간을 반복 --> for문
# 무한반복 + break ---> while문 

# i = int(input())

# while i >= 1:
#     print(i)
#     i += i
    
    

total = 0 

while True:
    n = int(input())

    if n == 0:
        print(total)
        break
    elif n < 0:
        print(total)
        total = 0
        
    else:
        total += n 



# total = 0 

# while True:
#     n = int(input())

#     if n == 0:
#         print(total)
#         break
#     elif n < 0:
#         print(total)
#         total = 0  # total을 초기화 
        
#     else:
#         total += n  # 합계누적 
