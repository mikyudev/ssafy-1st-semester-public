# def haha(num):
#     return print(str(num)[::-1])

# num = 12345
# haha(num)


'''
num = 12345
def haha(num):
     return(str(num)[::-1])

print(haha(num))

'''

num = 12345
def reverse_func(num):
     num = str(num) # 재할당
     num = num[::-1] # 거꾸로 슬라이싱 

     return num
    
result = reverse_func(num) # 함수호출 
print(result)