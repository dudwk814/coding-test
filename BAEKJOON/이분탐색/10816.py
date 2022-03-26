import sys

n = int(sys.stdin.readline())

d = list(map(int, sys.stdin.readline().split()))
d.sort()

m = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
data2 = [0] * m


def binary_search_left(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target:
            if mid == 0:
                return 0
            elif array[mid - 1] != target:
                return mid
            else:
                end = mid - 1
                continue

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def binary_search_right(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target:
            if mid == end:
                return end
            elif array[mid + 1] != target:
                return mid
            else:
                start = mid + 1
                continue

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):

    left = binary_search_left(d, data[i], 0, n - 1)
    right = binary_search_right(d, data[i], 0, n - 1)

    result = 0
    if left != None and right != None:
        result = right - left + 1
        print(result, end=' ')
    else:
        print(0, end=' ')
