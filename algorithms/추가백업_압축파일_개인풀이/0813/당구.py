import math

# 1. rad을 degree로  degree를 rad으로 바꾸는 법
print(math.pi) # 라디안 pi


degree = 30

rad = 30 * (math.pi / 180) # 라디안으로 바꿀 수 있음
print(rad)

rad = math.radians(degree)   # 30도 각도를 라디안으로 바꿈
print(rad)

degree = math.degrees(rad) # 다시 degree로 변환


################################################################################

# 2.  sin, cos, tan
print(f'{math.sin(rad):.1f}') # sin 30도
print(f'{math.cos(rad):.1f}') # cos 30도
print(f'{math.tan(rad):.1f}') # tan 30도

# .1f 는 출력하기 위해서 붙인거고 본 시험에서는 안 붙여도 됨


################################################################################

# 3.  피타고라스 정리 ( 두 변의 길이를 알았을 때 나머지 한 변의 길이 구하기)
# a = ??
b = 4
c = 5
# 식 a**2 + b**2 = c**2            | sqrt = 루트
# a**2 = c**2 - b**2
a = math.sqrt(c**2 - b**2)
print(a) # a의 길이 구하기



################################################################################



# 4. 삼각함수의 역함수  (변의 길이를 알고 각도를 알고싶을때 )
# 세타의 각도가 나옴
print(math.asin(a/c))
print(math.acos(b/c))
print(math.atan(a/b))          # 라디안 값



###############
# cos법칙 !
