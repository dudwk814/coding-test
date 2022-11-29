import sys
n, m = map(int, input().split())

array = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    sum_value = sum(array[i - 1: j])
    print(sum_value)
