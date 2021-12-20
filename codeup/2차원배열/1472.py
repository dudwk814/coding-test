# 2차원 배열 지그재그 채우기 2-5

n, m = map(int, input().split())
d = []
k = 0
for i in range(n):
    d.append([])
    for j in range(m):
        d[i].append(0)

for i in range(n):
    if n % 2 != 0:  # n이 홀수인경우
        for j in range(m):
            if i == 0:  # d[0][0 ~ m - 1]인 경우 n * m - j를 리스트의 반복 저장
                k = n * m - j
                d[i][j] = k
            elif i % 2 != 0:
                k = d[i - 1][m - 1] - m + j
                d[i][j] = k
            else:
                k = d[i - 1][m - 1] - m - j
                d[i][j] = k
    else:
        for j in range(m):
            if i == 0:  # d[0][0 ~ m - 1]인 경우 (n * m) - (m - 1) + j를 리스트의 반복 저장
                k = (n * m) - (m - 1) + j
                d[i][j] = k
            elif i % 2 != 0:
                k = d[i - 1][0] - 1 - j
                d[i][j] = k
            else:
                k = d[i - 1][m - 1] - m + j
                d[i][j] = k

for i in range(n):
    for j in range(m):
        print(d[i][j], end=' ')
    print()
