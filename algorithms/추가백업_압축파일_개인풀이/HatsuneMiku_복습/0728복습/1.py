# email = input()

# do = email.find('@')

# print(email[do + 1:])



# 함수로 변환하는 연습
def get_domain(email):
    
    idx = email.find('@')
    # 기호 없으면 "Invalid email" return
    if idx == -1:
        return "Invalid email"
    
    # @ 있으면 슬라이싱 return
    domain = email[idx + 1:]
    return domain

email = input()

result = get_domain(email)
print(result)



    # 기호 없으면 "Invalid email" return
    # @ 있으면 슬라이싱 return