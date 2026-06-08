import sys
sys.stdin = open('9386.txt')



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))


    max_v = 0
    cnt = 0
    for num in arr:
        if num == 1:
            cnt += 1

        else:
            if max_v < cnt:
                max_v = cnt
            cnt = 0


    if max_v < cnt:
        max_v = cnt
    print(f"#{tc} {max_v}")



    # max_v = 0
    # cnt = 0
    # for i in arr:
    #     if i == '1':
    #         cnt +=1
    #     else:
    #         cnt = 0
    #     cnt = 0
    #
    # if max_v < cnt:
    #     max_v = cnt
    # print(f"#{tc} {cnt}")