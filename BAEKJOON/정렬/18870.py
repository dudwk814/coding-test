import sys
n = int(sys.stdin.readline())

d = list(map(int, sys.stdin.readline().split()))
for i in range(len(d)):
    d[i] = (d[i], i)
d.sort()
index = 0
for i in range(len(d)):

    if i == 0:
        d[i] = (d[i][0], d[i][1], index)
    else:
        if d[i][0] == d[i - 1][0]:
            d[i] = (d[i][0], d[i][1], index)
        else:
            index += 1
            d[i] = (d[i][0], d[i][1], index)


d.sort(key=lambda x: x[1])

for i in d:
    print(i[2], end=' ')
