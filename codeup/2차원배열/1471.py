# 2차원 배열 지그재그 채우기 2-4
n = int(input())
d = []
k = n

for i in range(n):
    d.append([])
    for j in range(n):
        d[i].append(0)

for i in range(n):
    for j in range(n):

        if i == 0:  # d[0][0 ~ n -1]인 경우
            if j == 0:
                k = n - i
                d[i][j] = k
            elif j % 2 != 0:
                k = k - (n - 1) + n
                d[i][j] = k
            else:
                k = k + (n - 1) + n
                d[i][j] = k
        else:
            if j == 0:
                k = n - i
                d[i][j] = k
            elif j % 2 != 0:
                k = d[i - 1][j] + 1
                d[i][j] = k
            else:
                k = d[i - 1][j] - 1
                d[i][j] = k

for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print()
