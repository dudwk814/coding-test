import re
import sys
sys.setrecursionlimit(10000)
n = int(input())
array1 = list(map(int, sys.stdin.readline().split()))

m = int(input())
array2 = list(map(int, sys.stdin.readline().split()))


def binary_search(array, start, target, end):
    if start > end:
        return -2

    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif target < array[mid]:
        return binary_search(array, start, target, mid - 1)
    # 중간값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, target, end)


# print(array1)
for i in array2:
    print(binary_search(array1, 0, i, n - 1) + 1, end=' ')
