t = int(input())
num = list(map(int,input().split()))

num.sort() 

result= '' 

for i in num:
    result += str(i)

print(result)