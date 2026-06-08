# N, T = map(int,input().split())
#
#
# arr = list(range(1, N+1))
# for i in range(T):
#     a, b = map(int, input().split())
#
#     arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
#
# print(*arr)
################################################################
# N = 30
# arr = list(range(1, N+1))
# stack = []
# for _ in range(N-2):
#     a = int(input())
#
#     if a in arr:
#         arr.remove(a)
#
# print(*arr, sep='\n')
#
#
#
#
#
# N = 30
################################################################
# # 1. 비교의 기준이 될 '전체 숫자 세트'를 미리 만들어 둡니다.
# full_set = set(range(1, N + 1))
#
# # 2. 입력을 받아 '입력된 숫자 세트'를 만듭니다.
# # 예를 들어 28개를 입력받는다고 가정
# input_count = 28
# input_set = set()
#
# print(f"{input_count}개의 숫자를 입력하세요:")
# for _ in range(input_count):
#     a = int(input())
#     input_set.add(a)
#
# # 3. 루프가 모두 끝난 후, 단 한 번의 '차집합' 연산으로 빠진 숫자를 계산합니다.
# missing_numbers = full_set - input_set
#
# # 4. 최종 결과를 출력합니다.
# print("\n입력되지 않은 숫자:")
# print(sorted(list(missing_numbers)))
################################################################





################################################################
# 정렬 분할
################################################################
#
# def merge(left, right):
#     result = [0] * (len(left)) + (len(right))
#     l = r = 0  # 인덱스
#
#     # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result[l + r] = left[l] # result에 더 작을 걸 삽입
#             l +=1
#         else:
#             result[l+ r] = right[r]
#             r +=1
#     # 왼쪽 리스트에 남은 데이터들을 모두 result에 추가
#     while l < len(left):
#         result[l + r] = left[l]
#         l +=1
#     # 오른쪽 리스트에 남은 데이터들을 모두 result에 추가
#     while l < len(right):
#         result[l + r] = right[r]
#         r +=1
#
#     return result
#
#
#
#
# # 1. 분할
# # 2. 정복 & 병합(정렬)
#
# def merge_sort(li): # 병합정렬
#     if len(li) == 1:
#         return li
#
#     # 절반 씩 분할
#     mid = len(li) // 2
#     left = li[:mid]
#     right = li[mid:]
#     print(left, right)
#
#     left_list = merge_sort(left)
#     right_list = merge_sort(right)
#     # 여기까지 쪼개는 거
#     #########################################################################
#
#     merge_list = merge(left_list, right_list) # 이거 두개 병합만 해주면 됨
#     return merge_list



# arr = [69, 10, 30, 2, 16, 8, 31, 22]
# sorted_arr = merge_sort(arr)
# print(sorted_arr)




#########################################################################
# 퀵 정렬
#########################################################################

# pivot!  (기준) 가장 왼쪽에 있는 거
# pivot 기준으로 왼쪽에는 pivot 보다 작은 수
# 오른쪽에는 pivot 보다 큰수
# pivot 위치는 가운데로 오게 됨  ==> pivot은 이 시점에서 이미 정렬됨



# N = 10
# stack = []
# for i in range(N):
#     a = int(input())
#     b = a % 42
#     if b >= 0:
#         stack.append(b)
#
#
#
# print(len(set(stack)))



#
# N, M = map(int, input().split())
# arr = list(range(1, N+1))
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     arr[a-1:b] = arr[a-1:b][::-1]
#
# print(*arr)
#


# N = int(input())
# arr = list(map(int, input().split()))
#
# max_v = max(arr)
# stack = []
# for i in arr:
#     d = i/max_v*100
#     stack.append(d)
#
# print(sum(stack)/len(stack))

#
#
# n = input()
# print(int(n, 2))  # 2진수 문자열을 10진수로








