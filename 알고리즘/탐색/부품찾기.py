n = int(input())    # 동빈이네 부품 갯수
list1 = list(map(int, input().split()))  # 동빈이네 부품의 고유번호

m = int(input())  # 손님이 찾는 부품 갯수
list2 = list(map(int, input().split()))  # 손님이 찾는 부품의 고유번호

list1.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:    # 기준 값이 찾는 값과 같다면 리턴
        return mid
    elif array[mid] > target:  # 기준 값이 찾는 값보다 크다면 왼쪽을 탐색
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:  # 기준 값이 찾는 값보다 작다면 오른쪽을 탐색
        return binary_search(array, target, mid + 1, end)


for value in list2:
    result = binary_search(list1, value, 0, n - 1)

    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
