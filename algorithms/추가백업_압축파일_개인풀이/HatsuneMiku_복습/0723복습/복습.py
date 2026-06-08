# 출력하는 방법, 입력받는 방법 
# input()
# input은 실무에서 쓰지 않음 

# 1. 문자열 입력받기 
char = input()

# 2. 정수 입력받기 
num = int(input())

# 3. 정수 여러개 입력받아서 각각의 변수에 할당 
# map 함수, split() 메서드 
# map 함수를 쓰는 목적 : 정수로 변환 //// 문자를 입력받는다면 map 함수 필요x 
a, b = map(int, input().split())
print(a, b)

# 4. 정수 여러개를 입력받아서 리스트에 할당 
arr = list(map(int, input().split()))

print(*arr)

# 5. 심화 2차원 리스트를 입력받기 (D3)
# 3x3 행렬 
# 반드시 어떤 로직을 써야할까? : 중첩 반복문
# ---> 리스트 컴프리헨션 
'''
result = []
for _ in range(3): # 3행 
    arr = list(map(int, input().split()))
    result.append(arr) # 행 추가 행 추가, 행 추가 

print(result)
'''
arr = [list(map(int, input().split())) for _ in range(3)]

print(arr)