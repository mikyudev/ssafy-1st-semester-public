# 저글링 클래스 만들기 

class Zergling:
    # 생성자
    def __init__(self):
    # def __init__(self, hp, mana):
        # self.hp = hp
        # self.mana = mana
        self.hp = 20 # 인스턴스 변수, 속성, 필드 
        self.mana = 50

    # 메서드
    def run(self):
        print("뛴다")
        self.hp -= 1
        self.mana += 1 
    # 메서드 
    def show_status(self):
        print(self.hp, self.mana)


# z1 = Zergling(20,50)

z1 = Zergling()
z2 = Zergling()

z1.run()
z1.show_status()


for _ in range(5): #다섯번뛰고 
    z2.run()
z2.show_status() # 상태출력 


            ## 가장 기본적 클래스 구조 

            # 클래스, 스태틱, 매직   


class Calculator:
    pi = 3.141592 # 클래스 변수 

    # 생성자
    def __init__(self, name):
        self.name = name # 인스턴스 변수 

    # 메서드 
    def add(self, a, b):
        return a + b 
    
    # ★★★매직 메서드 ★★★ => 객체를 문자열로 표현할때 호출 됨 
    def __str__(self):
        return f'Calculator name : {self.name}'
    
    # 클래스 메서드 ---> 클래스 자체를 첫 번쨰 인자로 받는다 
    @classmethod
    def get_pi(cls):
        return f'파이 값은 {cls.pi}' # cls.pi = 클래스 변수  가져옴 
    
    # 스태틱 메서드 --> self 나 cls 가 없음, ★★★독립적 실행가능 
    @staticmethod
    def multiply(a, b):
        return a * b 
        

# 인스턴스 생성 (클래스 호출 전에 해야하는 거)
calc = Calculator("공학용 계산기")
# 메서드 호출
print(calc.add(2, 3))
# 매직 메서드 호출
print(calc)
# 클래스 메서드 호출 - 클래스로 직접 호출 
print(Calculator.get_pi())


# 스태틱 메서드 호출 - 클래스로 호출 가능, 인스턴스로 호출 가능 
print(Calculator.multiply(4, 5))
print(calc.multiply(4, 5))




# 상속 

# cla







# EAFP(try-except 구조) 예외처리 중심 
# - IndexError

def get_v(arr, idx):
    try:
        return arr[idx]
    except IndexError:
        return -1 # 인덱스 범위를 멋어난 경우 


arr = [1, 2, 3]
result = get_v(arr, 5)
print(result)


# LBYL (if - else 구조) 값 기준 

def get_v(arr, idx):
    if 0 <= idx <= len(arr) -1:
        return arr[idx] 
    return -1


arr = [1, 2, 3]
result = get_v(arr, 5)
print(result)
