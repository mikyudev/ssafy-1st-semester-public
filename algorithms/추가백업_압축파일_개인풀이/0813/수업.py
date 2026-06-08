

# 재귀
# n! = n * (n-1)!
#
# (n-1)! = (n-1) * (n-2)!
# (n-2)! = (n-2) * (n-3)!

# 2! =  2 *1!



#
#  피보나치
#
# n = int(input())
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(fibo(n))


# 계산 결과를 저장할 리스트 (메모)
# memo = {0: 0, 1: 1}
#
# def fibo_memo(n):
#     if n in memo:
#         return memo[n]
#     else:
#         # 계산한 적 없다면 계산해서 저장한 후 반환
#         result = fibo_memo(n-1) + fibo_memo(n-2)
#         memo[n] = result
#         return result
#
# n = int(input())
# print(fibo_memo(n))


########## 모든 배열 원소에 접근하는 재귀함수
#
# def f(i,N): # 크기 N인 배열 arr[i]에 접근
#     if i ==N: # 중단조건
#         return
#
#     else:   # 재귀호출
#         print(arr[i])
#         f(i+1, N)
#

####

#
# def fibo(n):         # 0 1 1 2 .....
#     global cnt
#     cnt +=1
#     if n <2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# cnt = 0
# print(fibo(10), cnt)
#
#
#
# def fibo1(n):
#     global cnt1
#     cnt1 += 1
#     if n>=2 and memo[n] == 0:
#         memo[n] = fibo1(n-1) + fibo1(n-2)
#     return memo[n]
#
# memo = [0] * 11
#
# memo[0] = 0
# memo[1] = 1
# cnt1= 0
#
# print(fibo1(10), cnt1)
#
#





######################################################

# stack, 재귀호출 (순열, 조합, 부분집합:비트연산)
#
# dfs

# sw 역랑테스트 다음주 화요일


# 3문제 2시간
# im 1문제 (im을 반드시 pass해야 a형을 풀 수 있음)
# a 형 2문제


# im 시험범위
# (스택, 큐, 재귀호출, dfs 절대 안 나옴)


#
# 1. 2차원리스트(범위 순회, 방향 배열, )
#     : 어려워지면 continue랑 break 잘 써야함
#     : for문 뿐만 아니라 while문도 잘 써야 한다 (while break)
#     : 함수 잘 만들어야 한다. (디버깅)  [ 평상시 연습 필요 ]
#     : 히든테케 100개 -> 80~90개 통과 나머지는 fail  ==> 디버깅


#
# 2. 그리디 알고리즘
#     : 나 완전탐색 좀 할줄아는데? 하고 풀어보면 시간초과
#     : N값 확인하고 N값이 100이상이다 그러면 4중 for문까지만 가능
#     : 완전탐색 x 그리디 !!!
#
#
# 3. Parsing (string)  9기  캡챠 코드
#     : find메서드 잘 쓰기
#     : 디버깅 잘 하기




# 야구 2, 4
# 어디에단어 ? 3
# 등산 1, 5









######################################## 괄호검사

#
# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     stack = []
#     for i in text:
#         # 1. 여는 괄호면 스택에 추가 (append)
#         if i =='{' or i =='(':stack.append(i)
#         # 2. 닫는 괄호가 중괄호면 스택이 비어있지 않고, 짝이 맞는지 확인 후 제거
#         elif stack and i =='}' and stack[-1] == '{': stack.pop()
#         # 3. 닫는 괄호가 소괄호면 스택이 비어있지 않고, 짝이 맞는지 확인 후 제거
#         elif stack and i ==')' and stack[-1] == '(': stack.pop()
#         # 4. 닫는 괄호인데 짝이 맞지 않다. -> stack에 추가 (append)
#         elif i =='}' or i ==')': stack.append(i)
#
#     if stack: result = 0 # stack이 비어있지 않으면
#     else: result = 1  # stack이 비어있으면 (괄호짝이 다 맞음)
#
#     print(f"#{tc} {result}")


#################################### 후위표기법
# 전략
# 피연산자 (숫자) 는 스택에 추가 (append)
# 연산자를 만나면 스택에서 두개의 숫자를 pop해서 계산
# (만약 스택에 2개의 숫자가 없다면 => error)
# 계산결과를 다시 스택에 추가 (append)
# 마지막 '.' 종료 , 스택에 딱 하나의 결과값만 있어야 함


# ex) 1 2 + 3 *
#
# 1. '1' -> 스택에 추가 : stack = [1]
# 2. '2' -> 스택에 추가 : stack = [1, 2]
# 3. '+' -> pop해서 2,1 계산 후 스택에 추가 append -> stack = [3]
# 4. '3' -> 스택에 추가: stack = [3, 3]
# 5. '*' -> 3, 3 pop해서 계산 후 스택에 추가 append -> stack = [9]
# 6. '.' -> 종료, 결과 return stack[0] == 9


# # T = int(input())
# #
# # for tc in range(1, T+1):
# #     expression = input().split()
# #     stack = []
# #     result = 'error'  # 기본 값 에러 설정
# #
# #     for token in expression:
# #         # 1. 토근이 숫자인 경우
# #         if token.isdigit():
# #             stack.append(int(token))  # 숫자로 변환해서 스택에 추가
# #
# #         # 2. 토근이 연산자인 경우
# #         elif token in "+-*/":
# #             # 연산할 숫자가 2개 미만이면 에러
# #             if len(stack) < 2:
# #                 break
# #
# #
# #             op2 = stack.pop()
# #             op1 = stack.pop()
# #
# #             if token == '+':
# #                 stack.append(op1 +op2)
# #             elif token =='-':
# #                 stack.append(op1 - op2)
# #             elif token =='*':
# #                 stack.append(op1 * op2)
# #             elif token =='/':
# #                 stack.append(op1 // op2) # 정수 나눗셈
# #
# #         # 마침표를 만난 경우
# #         elif token=='.':
# #             # 계산이 끝났을 때 스택에 숫자가 하나만 있어야 성공
# #             if len(stack) == 1:
# #                 result = stack.pop()
# #                 # 그 외의 경우는 모두 에러
# #             break
# #             # 숫자도, 연산자도, 마침표도 아닌 경우 (입력오류)
# #         else:
# #             break
# #
# #     print(f"#{tc} {result}")
# #
#
#
#
#
#
# def get_calculate(arr):
#     stack = []
#     for i in arr[:-1]: # 마지막을 element를 제외하고 순회
#         if i.isdecimal(): # 피연산자면 스택에 넣기
#             stack.append(int(i))
#         elif i in {'+', '-','*','/'}: # 연산자면
#             if len(stack) < 2: # pop을 해야되는데 2개 미만이면
#                 return 'error'
#             b = stack.pop()
#             a = stack.pop()
#             if i == '+': stack.append(a + b) # 계산해서 다시 스택에 넣기
#             elif i == '-': stack.append(a - b)
#             elif i == '*': stack.append(a * b)
#             elif i == '/': stack.append(a // b)
#
#     if len(stack) != 1:
#         return 'error'
#     return stack[0] # stack에 정수가 1개 있을 때
#
#
# T = int(input())
# for tc in range(1, T+1):
#     Forth = input().split()
#     result = get_calculate(Forth)
#     print(f"#{tc} {result}")
#
#
#





########################################################
# 재귀호출


# 완전탐색 ==> 다중 for 문 ! 한계 존재
# 그 한계를 극복 => 재귀호출

#
#
#
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
#
#
# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             for q in range(1,4):
#
#
#                 print(i, j, k, q, sep='')
#
#
#
#
#
# def get_cnt(n):
#     if n < 0:
#         return
#
#     cnt(n-1)
#
#     print(n, end = '')
#
#

    #########  이론

#
# def KFC(x):
#     print(x)      #8
#     x +=1
#     BTS(x + 5)
#     print(x)     #9
#
# def BTS(x):
#     print(x)  # 14
#
#
# x = 3
# KFC(x + 5)
# print(x) # 3



##### 함수의 특징
# 1. 값만 복사된다. !
# 2. 함수가 끝나면 함수를 호출했던 곳으로 돌아온다.


# def KFC(x):
#     if x == 2:
#         return
#     print(x)
#     KFC(x + 1)
#     print(x)
#
# KFC(0)



## 위는 재귀




# def KFC(x):
#     if x == 3:    # 깊이가 3  level
#         return
#     KFC(x + 1)
#     KFC(x + 1)
#     KFC(x + 1)
#     KFC(x + 1)          # branch 가 4
#     print(x)
#
# KFC(0)

#
# def KFC(x):
#     if x == 6:
#         return
#
#     KFC(x+1)
#     print(x)
#
# KFC(0)
#
#


'' \
''


def KFC(x):
    if x == 6:
        return
    print(x,end = ' ')
    KFC(x + 1)
    print(x, end=' ')

KFC(0)