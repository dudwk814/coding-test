import sys
import sys

n = int(input())

s = []

for i in range(n):
    name, k, e, m = sys.stdin.readline().split()

    k, e, m = int(k), int(e), int(m)
    s.append((name, k, e, m))

s.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for value in s:
    print(value[0])
