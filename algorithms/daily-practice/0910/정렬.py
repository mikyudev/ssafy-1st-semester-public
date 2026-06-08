
######################################################################
# 퀵 정렬
######################################################################
#
# def merge_sort(arr):
#     # 배열의 길이가 1이하면 이미 정렬이끝났다
#     if len(arr) == 1:
#         return arr
#     # 배열을 반으로 나누기
#     mid = len(arr) // 2
#     # 왼쪽 절반을 재귀적으로 정렬
#     left = merge_sort(arr[:mid])
#     # 오른쪽 절반을 재귀적으로 정렬
#     right = merge_sort(arr[mid:])
#     # 정렬된 왼쪽과 오른쪽 배열을 병합
#     result = merge(left, right)
#
#     return result
#
#
# def merge(left, right):
#     result = []
#     global cnt
#     i, j = 0, 0# i 는 왼쪽 , j는 오른쪽
#     if left[-1] > right[-1]: cnt += 1
#
#     # 왼쪽과 오른쪽배열을 비교하면서 병합
#     while i < len(left) and j <len(right):
#
#         if left[i] <= right[j]:
#             # 왼쪽요소가 더 작으니까 result에 append
#             result.append(left[i])
#             i += 1 # 인덱스 이동 (element 이동)
#
#         else:
#             result.append(right[j])
#             j += 1 # 그 다음 element이동
#
#     # while문이 종료되면 남은것들 extend
#     # if left[i:] > right[j:]: cnt +=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#
#     sorted_arr = merge_sort(arr)
#     print(f"#{tc} {sorted_arr[len(sorted_arr)//2]} {cnt}")








######################################################################
# 강사님
#
# def merge_sort(arr):
#     global cnt
#     # 배열의 길이가 1이하면 이미 정렬이 끝났다
#     if len(arr) <= 1:
#         return arr
#     # 배열을 반으로 나누기위한 인덱스
#     mid = len(arr) // 2
#     # 왼쪽 절반을 재귀적으로 정렬
#     left = merge_sort(arr[:mid])
#     # 오른쪽 절반을 재귀적으로 정렬
#     right = merge_sort(arr[mid:])
#     # 정렬된 왼쪽과 오른쪽 배열을 병합
#     result = merge(left, right)
#
#     return result
#
# def merge(left, right):
#     global cnt
#     result = []
#     i, j = 0, 0# i: 왼쪽, j: 오른쪽
#     # 왼쪽과 오른쪽배열을 비교하면서 병합
#
#     if left[-1] > right[-1]: cnt += 1
#
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             # 왼쪽 요소가 더 작으니까 result에 append
#             result.append(left[i])
#             i += 1 # element 이동(인덱스 이동)
#         else:
#             result.append(right[j])
#             j += 1 # 그다음 element 이동
#     # while문이 종료되면 남은것들 extend
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     sorted_arr = merge_sort(arr)
#     print(f'#{tc} {sorted_arr[N//2]} {cnt}')




######################################################################



#
# 1. 분할
# 1-1 피벗선택 (len(arr)//2)
# 1-2 피벗보다 작은건 left, 같은건 middle, 큰건 right
# 2. 정복 : 길이가 1이하면 return


# 문풀
# def quick_sort(arr):
#
#     if len(arr) <= 1:return arr
#
#     pivot = arr[len(arr) // 2 ]
#
#     left = [ x for x in arr if x < pivot]
#     middle = [ x for x in arr if x == pivot]
#     right = [ x for x in arr if x > pivot]
#
#     result = quick_sort(left) + middle + quick_sort(right)
#
#
#     return result
#
# # arr = [64, 34, 25, 12, 22, 11, 90]
#
# # sorted_arr = quick_sort(arr)
# # print(*sorted_arr)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     sorted_arr = quick_sort(arr)
#     print(f"#{tc} {sorted_arr[len(sorted_arr) // 2 ]}")


######################################################################

# # 강사님
# def merge_sort(arr):
#     global cnt
#     # 배열의 길이가 1이하면 이미 정렬이 끝났다
#     if len(arr) <= 1:
#         return arr
#     # 배열을 반으로 나누기위한 인덱스
#     mid = len(arr) // 2
#     # 왼쪽 절반을 재귀적으로 정렬
#     left = merge_sort(arr[:mid])
#     # 오른쪽 절반을 재귀적으로 정렬
#     right = merge_sort(arr[mid:])
#     # 정렬된 왼쪽과 오른쪽 배열을 병합
#     result = merge(left, right)
#
#     return result
#
# def merge(left, right):
#     global cnt
#     result = []
#     i, j = 0, 0# i: 왼쪽, j: 오른쪽
#     # 왼쪽과 오른쪽배열을 비교하면서 병합
#
#     if left[-1] > right[-1]: cnt += 1
#
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             # 왼쪽 요소가 더 작으니까 result에 append
#             result.append(left[i])
#             i += 1 # element 이동(인덱스 이동)
#         else:
#             result.append(right[j])
#             j += 1 # 그다음 element 이동
#     # while문이 종료되면 남은것들 extend
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     sorted_arr = merge_sort(arr)
#     print(f'#{tc} {sorted_arr[N//2]} {cnt}')

######################################################################

# 이진 탐색 먼저 sort하고 탐색
# start, middle, end 는 인덱스

# 1. 중간값 계산 : (start + end) // 2
# 2. 타겟이 중간값보다 작으면 왼쪽 부분 탐색 : end = mid -1
# 3. 타켓이 중간값보다 크면 오른쪽 부분 탐색

######################################################################

#
# def binary_search(arr, target):
#     start = 0
#     end = len(arr) -1
#
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return -1

# arr = [1, 3, 5, 7, 9, 11, 13 ,15, 17]
# target = 11
# result = binary_search(arr, target)

# print(result)





def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end: # start와 end가 같아질때까지
        mid = (start + end) // 2
        # 이진 탐색을 통해서 타겟을 찾으면 middle 인덱스 반환
        if arr[mid] == target:
            return mid
        # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
        elif arr[mid] < target:
            start = mid + 1
        else: # 타겟이 중간값보다 작으면 왼쪽 부분 탐색
            end = mid - 1
    # 타겟 못찾으면
    return -1

arr = [1, 3, 5, 7, 9, 11 ,13, 15, 17]
target = 11
result = binary_search(arr, target)
print(f'target index : {result}')







################################# 문제



def binary_search(arr, target):
    start = 0
    end = len(arr) -1
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
            flag = 1
        elif arr[mid] < target:
            if flag == 2: break
            flag = 2
            start = mid + 1
        else:
            if flag == 1: break
            flag = 1
            end = mid - 1

    return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = sorted(list(map(int, input().split())))
    target = list(map(int, input().split()))
    # flag = 0
    cnt = 0
    for t in target:
        cnt += binary_search(arr, t)

    print(f"#{tc} {cnt}")



