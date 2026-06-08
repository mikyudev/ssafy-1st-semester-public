H, M = map(int,input().split())

if M > 45:
    M -= 45

else:
    # M = M + (60 - 45)  ->  M += 15   =  M = M + 15
    M = 60 + (M - 45)      
    H -= 1
    if H < 0:
        H = 23

print(H ,M)












H, M = map(int,input().split())

if M >= 45:
   M =  M - 45

else: 
    M = M + (60 - 45)
    H -= 1 
    if H < 0: 
        H = 23

print(H, M)











