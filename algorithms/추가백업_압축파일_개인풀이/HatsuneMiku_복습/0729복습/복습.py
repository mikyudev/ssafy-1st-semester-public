# import requests 

# url = ''

# requests.get(url)


# dict 메서드의 .get
# .get   키로 벨류 조회하기 


# my_dict = {}



# for keys in my_dict: # 딕셔너리를 iterator 방식으로 순회 
#     print(keys)       # 어차피 key나와서 keys() 잘 안 씀 



 #  get이랑 items 많이 씀 

 # .get 과 .setdefault의 차이 
 # .setdefault는 k인 key가 없으면 추가해준다. 





seen = {1, 6, 3, 5, 9, 999 , -3, -10, 'A', 'B'}


a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)

# q)소스코드를 실행할 때마다 결과가 다를까? 같을까? 
# a)정수의 해시값은 일정하기 때문에 결과가 같다. 

# q) pop을 했을때 작은 값 먼저 제거하고 반환?? 
# a) x

# q) set의 요소에 문자가 있을때도 실행할 때마다 결과가 같을까? 다를까? 
# a) 정수의 해시값은 일정하고, 문자의 해시값은 일정하지 않다. 

set1 = {0, 1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}

set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)


# intersection 합집합 
# a issubet b   = b >= a 
# a issupperset b  =   a <= b 



arr = [1, 2, 3, 4, 5]
set1 = {1, 2, 3, 4, 5}

print(4 in arr ) # 전체를 순회 (느리다)
print (4 in set1) # 한 번에 찾는다 (해시 테이블)




a = { "a" : 2 , "b" : 3 , "c" : 4 }


print(a)
# print(a.items())

print(a.get("5", '없넹'))
print(a.items())

print(a.setdefault("5", "없당"))
print(a.items())

a.update( one = 4) 
print(a.items())
a.update( {'rtrt' : 3})
print(a.items())