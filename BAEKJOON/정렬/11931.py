import sys

n = int(sys.stdin.readline())
d = []
for i in range(n):
    d.append(int(sys.stdin.readline()))

d.sort(reverse=True)
for i in d:
    print(i)
