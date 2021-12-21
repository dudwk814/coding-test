# 지그재그 배열 2

n = int(input())
k = 0
d = []
for i in range(n):
    d.append([])
    for j in range(n):
        d[i].append(0)

for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                k = i + 1
                d[i][j] = k
            elif j % 2 != 0:
                k = d[i][j - 1] + (n - 1) + n
                d[i][j] = k
            else:
                k = d[i][j - 1] - (n - 1) + n
                d[i][j] = k
        else:
            if j == 0:
                k = i + 1
                d[i][j] = k
            elif j % 2 != 0:
                k = d[i - 1][j] - 1
                d[i][j] = k
            else:
                k = d[i - 1][j] + 1
                d[i][j] = k

for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print()
