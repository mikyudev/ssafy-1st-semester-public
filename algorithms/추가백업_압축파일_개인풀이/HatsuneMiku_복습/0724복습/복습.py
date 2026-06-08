############################

import math
PI = math.pi

print(math.ceil(PI)) #올림
print(math.floor(PI)) #버림
print(round(PI)) #반올림

# math. 붙이기 싫으면 

from math import ceil, floor, pi

print(ceil(PI)) 
print(floor(PI))
print(round(PI)) 



################### 별칭 

from math import ceil as olim

print(olim(PI))


#################

print(math.sqrt(9))  # 루트씌우기 

######################

from my_math import add

x = 2 
y = 3

print(add(x, y))

##############################

# pip install requests
# pip : python install packages          라이브러리 > 패키지 > 모듈 > 함수  
## 파이썬 버전과 호환되는 버전으로 자동 설치 


##################################
# numpy배열 
# numpy : 라이브러리 
# numpy.random : 패키지 
# numpy.random.nomal : 모듈 

############################################
# 조건문 
# if 의 '부정' elif 의 '부정' elif •••
#  


people = ["비비비","미미미"]


# 리스트를 순회하려고 한다 --> 파이써닉한 방식 : iterator 방식 
# for i in people:
#     print(i. end = ' ')


# for문은 언제쓰고 while문은 언제 써야 할까 

# 특정 구간을 반복 (ex) 2~6 까지)
# for문 쓰는게 나음
# 무한 loop 특정 조건에서 break
# while문 스는게 낫다 : while-break 

######################

arr = []
for i in range(5):
    arr.append(0)

print(arr)

# 파이써닉하다
arr = [0] * 5 


##################################
# for i in range(2, 10, 3):
# 이걸 while 문으로 바꿀 수 있어요?  

i = 2 
while i < 10:
    i += 3

    print(i, end = ' ')


print(i)


''' # while :  조건식이 참인동안 반복하는 반복문 
초기식 
while 조건식:
    code...
    증감식 
               ''' 


##########################

#  break continue  ★★★★★★
# break : 반복문 탈출
# continue : 반복문 처음으로 돌아가기 

# break 
# 백트래킹
