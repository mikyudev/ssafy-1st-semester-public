'''
num = 827364

def plus(num):
    num = str(num)
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])
    e = int(num[4])
    f = int(num[5])

    ee = (a%2 ==0) + (b%2 ==0) + (c%2 ==0) + (d%2 ==0) +(e%2 ==0) + (f%2 ==0) 
    dd = 6-ee
    return ee , dd

ee, dd = plus(num)
print(ee)
print(dd)
'''



    # def plus(num):
    # return = len(map(int(num)%2 ==0)), len(map(int(num)%3 ==0)

    # return (result)

    # print(plus(num))

num = 827364

def plus(num):
    num = str(num)
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])
    e = int(num[4])
    f = int(num[5])

    ee = (a%2 ==0) + (b%2 ==0) + (c%2 ==0) + (d%2 ==0) +(e%2 ==0) + (f%2 ==0) 
    dd = 6-ee
    return f"{ee}\n{dd}" 

print(plus(num))




# 전략 1번 
# num = str(num)
# digit1 = int(num[0]) # 100만
# digit2 = int(num[1]) # 10만


# 전략 2번 : 산술연산자 //, % 
num1 = 827364
def plus_1(num1):
    num1=int(num)
    digit1 = num // 100000 # 100만 
    digit2 = (num // 10000) % 10 # 10만 
    digit3 = (num // 1000) % 10
    digit4 = (num // 100) % 10
    digit5 = (num // 10) % 10
    digit6 = num % 10

    eee = (digit1%2 ==0) + (digit2 %2 ==0) + (digit3 %2 ==0) +(digit4 %2 ==0) +(digit5 %2 ==0) + (digit6 %2 ==0) 
    ddd = 6-eee

    return f"{eee}\n{ddd}"

print(plus_1(num1))
