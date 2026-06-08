
#
# def MIKU(x):
#     if x == 3:
#         return
#     MIKU(x+1)
#     MIKU(x+1)
#     print(x)
#
# MIKU(0)




# def MIKU(x):
#     if x == 6:
#         return
#     print(x,end = ' ')
#     MIKU(x+1)
#     print(x, end = ' ')
#
# MIKU(0)

#
# path = []
# def MIKU(x):
#     if x == 3:
#         if path[0]==path[1]==path[2]:
#             print(*path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         MIKU(x+1)
#         path.pop()
#
# MIKU(0)



# n = int(input())
#
# path = []
# used = [0] * 7
# def MIKU(x):
#     if x == n:
#         print(*path)
#         return
#
#     for i in range(1, 7):
#         if used[i] ==1: continue
#         used[i] = 1
#         path.append(i)
#         MIKU(x+1)
#         path.pop()
#         used[i] = 0
#
# MIKU(0)










#
#
#
# n = int(input())
# path = []
# cnt = 0
#
# def MIKU(lev, sum_v):
#     global cnt
#     if sum_v > 10:
#         return
#
#
#     if lev == n:
#         cnt +=1
#         # print(path)
#         # print(cnt)
#
#     for i in range(1, 7):
#         path.append(i)
#         MIKU(lev + 1, sum_v + i)
#         path.pop()
#
# MIKU(0, 0)
# print(cnt)













#
# n = int(input())
#
# path = []
# cnt = 0
# def MIKU(lev, sum_v):
#     global cnt
#     if sum_v > 10:
#         return
#     if lev == n:
#         cnt +=1
#
#     for i in range(1, 7):
#         path.append(i)
#         MIKU(lev+1, sum_v + i )
#         path.pop()
#
#
#
# MIKU(0,0)
# print(cnt)
#


arr = ['O', 'X']
path = []
name = ['miku', 'teto', 'furiren']


def print_name():
    for i in range(3):
        if path[i] =='O':
            print(name[i], end=' ')
    print()


def anime(lev):
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        anime(lev+1)
        path.pop()

anime(0)
