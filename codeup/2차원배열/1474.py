# 2차원 배열 지그재그 채우기 2-7

n, m = map(int, input().split())
d = []
k = 0

for i in range(n):
    d.append([])
    for j in range(m):
        d[i].append(0)

for i in range(n):
    for j in range(m):
        if m % 2 == 0:
            if i == 0:
                if j == 0:
                    k = (n * m) - (n - 1) + i
                    d[i][j] = k
                elif j % 2 != 0:
                    k = d[i][j - 1] + (n - 1) - n
                    d[i][j] = k
                else:
                    k = d[i][j - 1] - (n - 1) - n
                    d[i][j] = k
            elif i % 2 != 0:
                if j == 0:
                    k = (n * m) - (n - 1) + i
                    d[i][j] = k
                elif j % 2 != 0:
                    k = d[i - 1][j] - 1
                    d[i][j] = k
                else:
                    k = d[i - 1][j] + 1
                    d[i][j] = k
            else:
                if j == 0:
                    k = (n * m) - (n - 1) + i
                    d[i][j] = k
                elif j % 2 != 0:
                    k = d[i - 1][j] - 1
                    d[i][j] = k
                else:
                    k = d[i - 1][j] + 1
                    d[i][j] = k
        else:
            if i == 0:
                if j == 0:
                    k = (n * m) - i
                    d[i][j] = k
                elif j % 2 != 0:
                    k = d[i][j - 1] - (n - 1) - n
                    d[i][j] = k
                else:
                    k = d[i][j - 1] + (n - 1) - n
                    d[i][j] = k
            elif i % 2 != 0:
                if j == 0:
                    k = (n * m) - i
                    d[i][j] = k
                elif j % 2 != 0:
                    k = d[i - 1][j] + 1
                    d[i][j] = k
                else:
                    k = d[i - 1][j] - 1
                    d[i][j] = k
            else:
                if j == 0:
                    k = (n * m) - i
                    d[i][j] = k
                elif j % 2 != 0:
                    k = d[i - 1][j] + 1
                    d[i][j] = k
                else:
                    k = d[i - 1][j] - 1
                    d[i][j] = k


for i in range(n):
    for j in range(m):
        print(d[i][j], end=' ')
    print()
