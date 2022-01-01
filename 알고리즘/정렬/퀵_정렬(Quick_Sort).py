# # 퀵 정렬

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


# def quick_sort(array, start, end):

#     # 리스트의 원소가 1개라면 종료
#     if start >= end:
#         return

#     pivot = start
#     left = start + 1
#     right = end

#     while left <= right:

#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left += 1

#         # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1

#         if left > right:  # 엇갈렸다면 피벗과 작은 데이터를 교체
#             array[pivot], array[right] = array[right], array[pivot]
#         else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]

#     # 리스트를 분할 후 왼쪽과 오른쪽 리스트를 다시 정렬
#     quick_sort(array, start, right - 1)  # 왼 쪽
#     quick_sort(array, right + 1, end)  # 오른 쪽


# quick_sort(array, 0, len(array) - 1)


# print(array)


# 파이썬 퀵 정렬 코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있을 경우 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 리스트의 첫 번째 요소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 피벗을 기준으로 분할된(피벗보다 작은) 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 피벗을 기준으로 분할된(피벗보다 큰) 오른쪽 부분

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
