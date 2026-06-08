# 딕셔너리 : 가변비 시퀀스 
# 리스트에는 인덱스 -> 딕셔너리에는 key가 인덱스를 대신 
# 핵심★★ 딕셔너리는 비시퀀스이기때문에 key로 접근을 한다!


# 딕셔너리 초기화 2가지 방법 
# 1. 하드코딩
my_dict = {"apple":2, "banana":5, "peach":4}

# 2. key로 접근 
d = dict() # 빈 딕셔너리
d["apple"] = 2
d["banana"] = 5
d["peach"] = 4 

 
# d = {}   ---> 빈 딕셔너리 
# s = set() --->빈 세트

print(my_dict["banana"])

print(my_dict.keys()) # key만
print(my_dict.values()) 
print(my_dict.items()) # key랑 value 출력

