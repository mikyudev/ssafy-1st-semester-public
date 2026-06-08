numbers = list(map(int,input().split()))

max_value = max(numbers)

for index, value in enumerate(numbers):
    if value == max_value:
        print(index)
        break
    


# print(numbers.index(max(numbers)))

    