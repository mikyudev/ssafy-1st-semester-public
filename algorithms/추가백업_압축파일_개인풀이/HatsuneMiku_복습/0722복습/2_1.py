list = [1, 5, 2, 7, 3, 6]

print(*list)
print(*list[0:1],*list[:-2:-1])
print(*list[1::2])
print(*list[::-1])



# gpt 정답 !! 

arr = [1, 5, 2, 7, 3, 6]

print(*arr)
print(arr[0], arr[-1])
print(*arr[1::2])
print(*arr[::-1])


print(arr[0], arr[-1])
print(arr[0], arr[len(arr) - 1]) #얘네는 없어도되네? 


print(*arr[1:len(arr):2])  #짝수번째 
print(*arr[1::2])

print(*arr[::-1])


##################################
#  element = 요소 [1] , [2] .... 
arr=[1, 2, 3, 4] 
print(id(arr))

arr[3]= 7 # 재할당 x 
print(id(arr))  # 메모리주소가 같음 
# 주소값 재할당 하려면 아예 새로 LIST 만들어야함 

arr = [1, 2, 3] # 재할당 o 
print(id(arr)) # 메모리 주소가 다르다

# ★★★ 리스트의 element만 가변했을 때 재할당이 이루어 지지 않는다. 

