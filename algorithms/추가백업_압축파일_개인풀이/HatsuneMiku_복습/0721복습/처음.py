print('hello', end= ' ')
print('world')

print('hello', 'world')

degree = 36.5    # 36.5[값] =[할당연산자] degree[변수]에 할당되었다 o 저장되었다 x 
print(id(degree)) 

degree = 36.6   
print(id(degree))  


# Alt + shift + 방향키 = 복사 
# ctrl + b = 사이드바 
# ctrl + ~ = 터미널 
# ls => python 파일이름 = 실행 
# ctrl + / = 주석처리

#   print (내장함수) => sep 공백, end 줄바꿈  |  바꾸려면 위에처럼 


# /////////////////////////////////////////////////////////////////////////////


rbrbtjdtjd = 20 
_rbrbtjd = 20 

lst = [1, 2, 3]
# sum = 7    -> 오류 
print(sum(lst)) 

# list = [1, 2, 3, 4]
# arr = list((1, 2, 3, 4))
# print(arr)


# 변수명 규칙 : 숫자로 시작할 수 없다. 
# 언더스코어 가능 _ 
# 키워드 사용 불가능 (if, for)
# 내장함수나 매서드 가급적 사용 하지 않는다 





# 유니코드 출력 내장함수 
# 대소문자는 서로 다른 유니코드값을 가지고 있다. 
print(ord('A')) #65
print(ord('a')) #97





a = 2       # 정수(int) : 양의정수, 음의정수, 0
b = 2.0     # 실수(float) : .@ 붙으면 무조건 실수처리 (2.0, 3.0 ... )
c = 3 + 2j  # 복소수(허수) [ 아예 안 씀 ]
d = '1'


print(a == b) # 타입은 다른데 값은 같다고 나옴 True 

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# 1억을 지수표현법  - 잘 안 씀 
num = 1e8
print(num)

# 연산자 우선순위 => 시험 
# ** 

a = '1'
print(str(a))

char = "hello world" # 문자형 자료는 순서가 있다 -> 인덱스가 있다 -> [ 0 : 0 : 0]
                       # ↑
space = ' '            # ↑
print(ord(space)) # 공백 자체도 유니코드 값을 가진다. 



#
print("\"안녕하세요\"")




#
name = '이'
age = 20 
height = 177.12

print(f'이름은 {name}이고, 나이는 {age}살, 키는 {height:.1f}')

#소수 n째 자리 까지 반올림 :.nf 


# char[start:stop:step]
# 1. step이 양수 
# start 부터 end -1 까지 

# 2. step이 음수 
# start 부터 end +1 까지 

# ☆★ 항상 end 를 포함하지 않는다 ★☆

'''여러 줄 
주석 
입
니
다
'''