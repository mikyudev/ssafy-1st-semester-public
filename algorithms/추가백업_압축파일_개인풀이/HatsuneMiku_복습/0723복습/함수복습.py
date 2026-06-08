# 함수 : 나만의 명령어 만들기
# ex) a와 b를 입력받으면 이 두 변수를 더해라 
# ex) 리스트를 입력받고 각 element의 최대값을 구해라 

# parameter와 argument 차이점?? 

'''
# 함수정의 
def 함수명 (parameter):
    snake - case
    code ......

    return 반환값 있어도 되고 없어도 됨        -> 나만의 명령어 제작 

# 함수호출 
        함수명 (argument)                 -> 명령을 했다. 
        '''

# parameter = input
# argument = output  호출 



############################ 
# * 애스터리스크  1개 = tuple ,  2개 = dict 

#######################
# 재귀 함수란? 
# 이 함수가 재귀함수다 ! 어떻게 알 수 있을까? 
# 재귀 호출( 자기자신을 호출)이 있으면 재귀 함수 
# 단 주의 : 무한loop에 빠질 수 있다. 
# 무한 loop를 막으려면? 2. 기저 조건(종료조건)[return]

def kfc(lev):
    # 2. 기저 조건
    if lev == 2:  # (2) 
        return   # (7) 
    print(lev)   # (3)
    # 1. 재귀 호출 
    kfc( lev+1 )  # (4)
    kfc( lev+1 )  # (5) 
    print(lev)   # (6) 

kfc(0) #(1) 

# 함수의 특징 2가지 
# 1. 값만 복사가 된다
# 2. 함수의 호출했던 곳으로 돌아온다. 

'''
# while True - break 
# for - break 
'''


##################
# sort()와 sorted() 의 차이 
# 공통점 : 정렬 (오름차순) 

arr = [1, 2, 3, 4, 5]

# 반환 x , 원본 변경 ---> sort() 
arr.sort #(reverse=True) 내림차순 
# 반환 o , 원본 변경 x ----> sorted() 
sorted_arr = sorted(arr) #(reverse=True) 내림차순 


#######################


a = 30 # global scope # 10

def kfc():
    global a # global 쓰는 목적? # 전역번수를 수정하고 싶을 때 
    a = 10 # local scope 
    b = 20
    print(a) # 10

kfc()
print(a) # 10  # built-in scope  파이썬 가장 바깥쪽 scope 


#######

# ★★★★★★LEGB !!!! 중요!!!!!

# 글로벌 키워드 쓰는 이유 = 전역변수 수정을 위해 

# 함수이름 작성 규칙 7자만 기억하자 
# # snake_case


##############################
# 람다 , 파라미터, 함수식  끝 

