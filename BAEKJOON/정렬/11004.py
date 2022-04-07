import sys

n, k = map(int, sys.stdin.readline().split())

d = list(map(int, sys.stdin.readline().split()))

d.sort()
print(d[k - 1])
