import sys

n = int(input())
m = int(input())

array = list(map(int, sys.stdin.readline().split()))

array.sort()
idx = 0
for i in array:

    sub_score = m - i

    if sub_score > i:
        if sub_score in array:
            idx += 1


print(idx)
