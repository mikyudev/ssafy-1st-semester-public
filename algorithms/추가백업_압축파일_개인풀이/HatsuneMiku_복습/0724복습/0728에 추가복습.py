def get_sum(x, y):
    pass
# 함수에 pass 많이 넣어서 활용 함 


# map 함수
# zip 함수 (엄청 많이는 안 씀)


print(zip)

# for break else 구조 for문 정상적으로 끝나야 else 실행 아니면 break에서 걍 끝 

# break continue 같이 씀 


# enumerate(iterable, star=0) 인덱스와 값을 함께 반환하는 내장함수 

'''
 numbers = list(map(int,input().split()))

 max_value = max(numbers)

 for index, value in enumerate(numbers):
     if value == max_value:
         print(index)
         break
'''

#  최대값 초기화 (문제에서 음수가 input으로 없을 때는 0으로 초기화)
# max_v = 0 
# 최대값의 범위가 문제에 주어지지 않을 때 



# ★★★★★★★★★★★ 외워야 함 
max_v = float('-inf') # 음의 무한대
# min_v = float('inf') # 양의 무한대 

for idx, value in enumerate(arr):
    #최대값 코드
    if value > max_v:
        max_v = value # 최대값 갱신 + 되었을때 
        result = idx # 그 때의 인덱스 

print(result)


# 단 max, sum, len 내장함수를 쓰지마시오 등으로 월말이 나옴 그때 유용