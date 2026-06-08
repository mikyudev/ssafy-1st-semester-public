# for tc in range(1, 11):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#
#     total = 0
#     for i in arr[2::2]:
#         idx = arr.index(i)
#         if i > max(arr[idx-1], arr[idx-2], arr[idx+1], arr[idx+2]):
#             a = i - max(arr[idx-1], arr[idx-2])
#             b = i - max(arr[idx+1], arr[idx+2])
#             total += min(a, b)
#
#         else: continue
#
#
#     for i in arr[3::2]:
#         idx = arr.index(i)
#         if i > max(arr[idx-1], arr[idx-2], arr[idx+1], arr[idx+2]):
#             a = i - max(arr[idx-1], arr[idx-2])
#             b = i - max(arr[idx+1], arr[idx+2])
#             total += min(a, b)
#         else: continue
#
#
#
#     print(f"#{tc} {total}")
#




#
# arr = list(map(int, input().split()))
#
# print(arr[2::2])
# print(arr[3::2])
# for テストケース in range(1, 11):
#     N = int(input())
#     初音ミク = list(map(int, input().split()))
#     トータル = 0
#
#     for i in range(2,N-2):
#         miku = max(初音ミク[i-2],初音ミク[i-1])
#         teto = max(初音ミク[i+1],初音ミク[i+2])
#
#         高さだぜ = 初音ミク[i] - max(miku, teto)
#
#         if 高さだぜ > 0:
#             トータル += 高さだぜ
#
#
#     print(f"#{テストケース} {トータル}")

#
# こんにちは = int(input())
# for テストケース in range(1, こんにちは+1):
#     七つの大罪 = int(input())
#
#     時間 = [tuple(map(int, input().split())) for _ in range(七つの大罪)]
#     時間.sort(key=lambda x: (x[1],x[0]))
#
#
#     みかんうまい = 0
#     最後の時刻 = 0
#
#     for スタート, 最後  in 時間:
#         if スタート >= 最後の時刻:
#             みかんうまい +=1
#
#             最後の時刻 = 最後
#
#
#     print(f"#{テストケース} {みかんうまい}")



#
# arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
#
# idx = int(input())
#
# print(sum(arr[idx:idx+5]))








def get_sum(arr):
    total = 0
    max_idx = 0
    max_v = 0
    for i in range(len(arr)-4):
        total = sum(arr[i:i+5])

        if max_v < total:
            max_v = total
            max_idx = i

    return max_idx
arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13, 45, 45,45, 4,5 ,45,45,45,454,545,454,55,4545,4 ]
print(get_sum(arr))


