t = int(input())


def countPeople(k, n):
    d = [[0 for _ in range(n)] for _ in range(k + 1)]

    for i in range(k + 1):
        for j in range(n):
            if i == 0:
                d[i][j] = j + 1
            else:
                if j == 0:
                    d[i][j] = 1
                else:
                    d[i][j] = d[i][j - 1] + d[i - 1][j]
    print(d[k][n - 1])


for i in range(t):
    k = int(input())
    n = int(input())
    countPeople(k, n)
