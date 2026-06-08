# 언팩킹 연산자 


temps = [0, 20, 30, 37, 100]

def C(temps):
    C = list(map(lambda x: x * 9/5 + 32, temps))
    return C

print(C(temps))
print(*C(temps))






temps = [0, 20, 30, 37, 100]

def C(temps):
    C = map(lambda x: x * 9/5 + 32, temps)
    return C

print(*C(temps))