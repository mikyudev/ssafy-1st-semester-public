

arr = [list(map(int,input().split())) for _ in range(9)]

result_y = -1
result_x = -1 
max_v = float('-inf')
for y in range(9):
    for x in range(9):
        if max_v < arr[y][x]:
            max_v = arr[y][x]
            result_y = y+1 
            result_x = x+1
print(max_v)
print(result_y, result_x)