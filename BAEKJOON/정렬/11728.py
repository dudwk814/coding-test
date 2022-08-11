import sys

n, m = map(int, input().split())

n = list(map(int, sys.stdin.readline().split()))
m = list(map(int, sys.stdin.readline().split()))

s = n + m

s.sort()

print(*s)