import sys
n = int(sys.stdin.readline())
d = [0] * 10001

for i in range(n):
    input_data = int(sys.stdin.readline())
    d[input_data] += 1

for i in range(1, len(d)):
    if d[i] != 0:
        for j in range(d[i]):
            print(i)
