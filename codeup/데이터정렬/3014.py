import sys

n = int(sys.stdin.readline())


array = list(map(int, sys.stdin.readline().split()))
count = [0] * (max(array) + 1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            print(i, end=' ')
