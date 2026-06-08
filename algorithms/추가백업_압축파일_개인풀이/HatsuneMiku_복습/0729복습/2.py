# t = map(int,input().split())

# num_set = set()

# if len(set(t)) == 6:
#     if all(1<= num <= 45 for num in t):
    
#         print('VALID')

#     else:
#         print('INVAID')
# else:
#     print('INVAID')

     




# nums = list(map(int,input().split()))

# num_set = set()
# for num in nums:
#     if not (1<= nums <= 45):
#         print("INVALID")
#         break
#     num_set.add(num)

# else:
#     if len(num_set) == 6:
#         print("VALID")

#     else:
#         print('INVALID')



numbers = list(map(int,input().split()))

lotto = set()
for num in numbers:
    if 1 <= num <= 45:
        lotto.add(num)

if len(lotto) == 6:
    print('VALID')
else:
    print('INVALID')