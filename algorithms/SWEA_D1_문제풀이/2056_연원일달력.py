t = int(input())

day_dic = {1: 31, 2: 28, 3: 31, 4: 30,
       5: 31, 6: 30, 7: 31, 8: 31,
       9: 30, 10 : 31, 11: 30, 12: 31}


for case in range(1, t+1):
    day = input()

    year = day[:4]
    month = int(day[4:6])
    day = int(day[6:])

    if 1<=month<=12 and 1 <= day <= day_dic[month]:
        print(f"#{case} {year}/{month:02}/{day:02}")
    else:
        print(f"#{case} -1")


# print(f"#{case} {year}/{month:02}/{day:02}")
# print(f"#{case} {year}/{date[4:6]}/{date[6:]}")
