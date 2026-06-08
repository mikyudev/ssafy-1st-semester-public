# ##############################################################################################
# ##############################################################################################
#
# import heapq
#
#
# pq = [5, 2, 8, 1, 9]
#
# heapq.heapify(pq)
#
# sorted_arr = []
#
# for i in range(len(pq)):
#     sorted_arr.append(heapq.heappop(pq))
#
# # print(pq)
# print(sorted_arr)
#
# ##############################################################################################
# # 최대 힙 = 부호반전을 씀
# ##############################################################################################
# import heapq
#
# pq = [5, 2, 8, 1, 9]
# stack = []
# for x in pq:
#     heapq.heappush(stack, -x)  # 음수로 저장
#
#
#
# while stack:
#     print(-heapq.heappop(stack), end=" ")  # 9 8 5 2 1
#
# ###############################################################################################
#
# import heapq
#
# pq = [5,2, 8, 1, 9]
#
# stack = []
# for x in pq:
#     stack.append(-x)
#
# pq = stack
#
# heapq.heapify(pq)
#
# rev_sorted = []
# for i in range(len(pq)):
#     rev_sorted.append(-heapq.heappop(pq))
#
# print(rev_sorted)
#
# ###############################################################################################
# # 다중조건
# ###############################################################################################
#
# import heapq
#
# pq = [5, 2, 8, 1, 9, 4]
#
# stack = []
#
# for num in pq:
#     if num % 2 == 0:
#         heapq.heappush(stack, (0, num))
#
#     else:
#         heapq.heappush(stack, (1, num))
#
#
# h = []
# while stack:
#     p, num = heapq.heappop(stack)
#     h.append(num)
#
# print(*h)
#
#
# ###############################################################################################
# # 다중조건
# ###############################################################################################
#
#
# import heapq
#
# pq = [(7,'A'), (9,'C'), (7, 'C'), (6,'D'), (5, 'A')]
#
# heap = []
# for num, ch in pq:
#     # (문자, -숫자, 원래값) 형태로 넣기
#     heapq.heappush(heap, (ch, -num, num))
#
# result = []
# while heap:
#     ch, neg_num, num = heapq.heappop(heap)
#     result.append((num, ch))
#
# for num, ch in result:
#     print(f"({num}, {ch})", end=" ")
#
# ###############################################################################################
# # 다중조건
# # 우선순위 큐를 이용한 정렬을 하려고 합니다.
# #
# # 우선순위 조건은 다음과 같습니다.
# #
# # 1. 작은 수 우선
# # 2. 큰 문자 우선
# #
# # 처리과정은 다음과 같습니다.
# #
# # 1. 정수 n을 입력받습니다.
# # 2. n번 반복하면서
# #    2-1. 힙에서 하나를 꺼냅니다
# #    2-2. 꺼낸 숫자에 2를 곱한 후 17로 나눈 나머지를 구합니다.
# #    2-3. 계산된 새로운 숫자와 원래 문자를 힙에 다시 넣습니다
# ###############################################################################################
# import heapq
#
# pq = [(9,'A'), (8,'B'), (9,'A'), (10,'C'), (15,'A')]
#
#
# h = [ ]
# for num, ch in pq:
#     heapq,heapq.heappush(h, (num, -ord(ch), ch))
#
# n = int(input())
# for _ in range(n):
#     num, _, ch = heapq.heappop(h)
#     num = (num*2) % 17
#     heapq.heappush(h, (num, _, ch))
#
#
# result = []
#
# while h:
#     num, _, ch = heapq.heappop(h)
#     result.append((num, ch))
#
# for num, ch in result:
#
#     print(f"({num}, {ch})", end =" ")
#
#
# ###############################################################################################
# # final
# ###############################################################################################
#
# import heapq
#
# arr = [
#     (2, "BHC"),
#     (1, "NeNe"),
#     (3, "KFC"),
#     (1, "BBQ"),
#     (2, "Moms"),
#     (4, "Mc"),
# ]
#
# heapq.heapify(arr)
#
# while len(arr) > 1:
#     len1, name1 = heapq.heappop(arr)
#     len2, name2 = heapq.heappop(arr)
#
#     new_len = len1 + len2
#     new_name = min(name1, name2)
#
#     heapq.heappush(arr, (new_len, new_name))
#
# final_len, final_name = heapq.heappop(arr)
#
# print(final_name, final_len)
#
# ###############################################################################################
#
# import heapq
#
# # 초기 개체들: (길이, 이름)
# creatures = [
#     (2, "BHC"),
#     (1, "NeNe"),
#     (3, "KFC"),
#     (1, "BBQ"),
#     (2, "Moms"),
#     (4, "Mc"),
# ]
#
# # h = []
# # for length, name in arr:
# #     heapq.heappush(h, (length, name))
#
# heapq.heapify(arr)
#
# while len(arr) > 1:
#     len1, name1 = heapq.heappop(arr)
#     len2, name2 = heapq.heappop(arr)
#
#     new_len = len1 + len2
#     new_name = name1 if name1 < name2 else name2  # 사전순으로 앞선 이름
#
#     heapq.heappush(arr, (new_len, new_name))
#
# final_len, final_name = heapq.heappop(arr)
# print(final_name, final_len)
#

###############################################################################################
###############################################################################################


'''
n = int(input())
scores = [500] # 초기값 500

for _ in range(n): # N
    a, b = map(int, input().split())
    scores.append(a)
    scores.append(b)
    scores.sort() # NlogN

    length = len(scores)
    mid = scores[length // 2]

    print(mid)

# 시간복잡도 O(N제곱 logN)
'''

import heapq

max_heap = [] # 내림차순 중간값 보다 작은값 (최대힙)
min_heap = [] # 오름차순 중간값 보다 큰값 (최소힙)
mid = 500

def push(v):
    if mid > v: # 중간값 보다 작으면 최대 힙에 추가
        heapq.heappush(max_heap, -v)
    else: # 중간값보다 크거나 같으면 최소 힙에 추가
        heapq.heappush(min_heap, v)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    # 경우가 두가지 1. 왼쪽이 더 많을 경우 (최대힙의 크기가 더 클경우)
    # 2. 오른쪽이 더 많을 경우 (최소힙의 크기가 더 클경우)

    if len(max_heap) > len(min_heap):
        # 최대힙이 많으니까 최소힙에 넣기 (갯수맞추기)
        heapq.heappush(min_heap, mid)
        # 최대 힙에서 가장 큰값 꺼내서 새로운 중간값으로 설정
        mid = -heapq.heappop(max_heap)
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)
        mid = heapq.heappop(min_heap)

    print(mid)

# 시간복잡도가 NlogN