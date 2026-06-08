# import requests

# dummy_data = []

# for user_id in range(1, 11):
#     response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
#     parsed_data = response.json()
#     name = parsed_data['name']
#     dummy_data.append(name)

# print(dummy_data)


import requests
from pprint import pprint
# API_URL = 'f'https://jsonplaceholder.typicode.com/users/{user_id}'

# response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
# parsed_data = response.json()

# print(response)
# print(parsed_data)

dummy_data = [] 

for user_id in range(1, 11):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    parsed_data = response.json()
    name = parsed_data['name']
    dummy_data.append(name)

pprint(dummy_data)


# name = []
# for name in dummy_data:
    
#     print(name)
