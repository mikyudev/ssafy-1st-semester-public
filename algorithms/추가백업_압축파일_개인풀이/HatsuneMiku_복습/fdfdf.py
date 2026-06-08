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