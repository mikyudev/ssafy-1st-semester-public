# find 매서드

# 이론 2가지 
# ★1. str.find() : str에서 특정 문자나 문자열을 찾아주는 메서드
# 찾으면 첫 번째로 발견된 인덱스 반환, 못찾으면 -1 
# ★★★★★2. str.find('a', n) ★★★★★  n = 정수 
# : n번째 인덱스 이후부터 시작해서 'a'문자를 찾아라!!!!!!  

text = 'B[45]AB[2234]'
start1 = text.find('[')
end1 = text.find(']', start1 +1)
start2 = text.find('[', end1 +1)
end2 = text.find(']', start2 +1)

print(start1)
print(end1)
print(start2)
print(end2)


# 유니코드 
# 알파벳의 유니코드 ---> 아스키코드 

# 암기 2개  32차이 남  
#  'A'  == 65
#  'a'  == 97

char1 = 'k'# 대문자 
char2 = ord(char1) + 32 # 소문자 

print(chr(char2))

# split, join 중요

'''
text = "sangho.jang"

text2 = text.replace("sangho", "lee")

print(text)
print(text2)  #원본은 안 바뀜 불 변 

'''

# 리스트 
# element 한개 추가 -->  append - 맨 뒤에 추가  
# iterable 추가 --> extend - 리스트에 iteralbe 추가 [for문 돌려도 됨 ]
# pop() --> 맨 끝 element 제거, ★반환★
# pop(0) --> 맨 앞 element 제거, ★반환★




##################count
arr = [1, 2, 3, 4, 4, 2, 1]

print(arr.count(1))


# 위에처럼 해도 되는데 밑에처럼을 할 수 있어야함 

cnt = 0 
for i in arr:
    if i == 1: 
        
        cnt +=1

print(cnt)


########################reverse 대체 
arr = [1, 2, 3, 4, 5]
arr2 = arr[::-1]
print(arr2)



############## append

arr = []
arr.append(1)  #arr = [1] 
arr.append(2)  #arr = [1, 2] 
arr.append(3)  #arr = [1, 2, 3]

arr.pop()     # arr = [1, 2, 3]  #나중에 들어온게 먼저 빠진다 (stack) 

arr.pop(0)     # arr = [1, 2, 3]  #먼저 들어온게 먼저 빠진다 (queue) 




# arr = [1, 2, 3, 4, 5]

# arr = [2, 3, 4, 5, 1]
# while True:
#     n = int(input())

#     for i in range(n)
#     front = arr.pop(0)
#     arr.append(front)


#     print(arr[0])

## 위에 queue 문제 



############################ sort () 


# sort 와 sorted차이 반환값이 없는지 있는지 (원본이 변경 되는지 안 되는지) 
# 즉 원본을 변경하기 싫으면 sorted() 써야함. 

arr = [3, 2, 5, 1, 4]

arr.sort() # 오름차순 

print(arr)

arr.sort(reverse=True) # 내림차순 

print(arr)


############# 얕은, 깊은 복사 

'''
arr = [1, 2, 3]

arr2 = arr[:] # 얕은 복사 

arr2.append(4)

print(arr)
print(arr2)
'''


import copy


arr = [1, 2, [3, 4, 5]]

# arr2 = arr[:] # 얕은 복사의 한계 (복사본이 변경되었을 때 원본이 변경)
arr3 = copy.deepcopy(arr) # 깊은복사 (복사본 변경되어도 원본 변경 x )

# arr2[2][0] = 999
arr3[2][0] = 999 

print(arr)
print(arr3)




###########################################################################
# list comprehension  

# 2차원 배열 생성 시 (인접행렬 생성)
result = [] 
arr = [0] * 5 
for _ in range(5):
    result.append(arr)
print(result)

arr = [[0] * 5 for _ in range(5)]
print(result)

# 2차원 배열 입력 (n행)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

################### 메서드 체이닝 



a = { "a" : 2 , "b" : 3 , "c" : 4 }

print(a.items())