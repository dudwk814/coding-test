import sys

n = int(sys.stdin.readline())
d = list(set(map(int, sys.stdin.readline().split())))
d.sort()
print(*d)
