import requests

url ='https://date.nager.at/api/v3/publicholidays/2025/KR'

response = requests.get(url).json() # dict 
response = requests.get(url).text #  json 

# json 과 dict 공통점 
# key : value 쌍 

# 차이점 
# json은 반드시 key값이 문자열, 큰따옴표 ,true, false

# json 파싱을 어떻게 할까??? 
# 1. 터미널로 출력결과를 확인하기에는 가독성이 많이 떨어진다. ---> viewer로 확인한다. 
# json을 viewer로 복사 붙여넣기 하고 확인(parsing 준비)

print(response)