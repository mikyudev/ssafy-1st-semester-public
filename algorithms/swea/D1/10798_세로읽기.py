

arr = [list((input().rstrip())) for _ in range(5)]

max_len = max(len(row) for row in arr)
arr2 = []       

for x in range(max_len):
    for y in range(5):
        if x < len(arr[y]):
            arr2.append(arr[y][x])
        

print(''.join(arr2))