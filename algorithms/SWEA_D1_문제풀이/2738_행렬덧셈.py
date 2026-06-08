
N, M  = map(int,input().split())

arr1 = [list(map(int,input().split())) for _ in range(N) ]
arr2 = [list(map(int,input().split())) for _ in range(N) ]



for y in range(N):
    for x in range(M):
        arr2[y][x] += arr1[y][x]
    
    result = arr2[y][x]
# print(arr2)

for row in arr2:
    print(*row)

# for i in range(N):
# row = [A[i][j] + B[i][j] for j in range(M)]
# print(*row)