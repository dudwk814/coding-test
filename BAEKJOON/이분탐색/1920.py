import sys
n = int(sys.stdin.readline())

d = list(map(int, sys.stdin.readline().split()))
d.sort()

m = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))


def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):

    if binary_search(d, data[i], 0, n - 1) != None:
        print(1)
    else:
        print(0)
