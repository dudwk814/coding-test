# 2차원 배열 지그재그 채우기 2-6

n, m = map(int, input().split())
d = []
k = 0

for i in range(n):
    d.append([])
    for j in range(m):
        d[i].append(0)

for i in range(n):

    for j in range(m):
        if n % 2 != 0:  # n이 홀수인 경우
            # d[0][0 ~ m - 1]인 경우 (n * m) - (m - 1) + j를 리스트에 반복 저장 (1씩 증가)
            if i == 0:
                k = (n * m) - (m - 1) + j
                d[i][j] = k
            # d[짝수][0 ~ m - 1]인 경우 d[i - 1][0] - 1 - j를 리스트에 반복 저장 (1씩 감소)
            elif i % 2 != 0:
                k = d[i - 1][0] - 1 - j
                d[i][j] = k
            else:  # 나머지인 경우 d[i - 1][m - 1] - m + j를 리스트의 반복 저장 (1씩 증가)
                k = d[i - 1][m - 1] - m + j
                d[i][j] = k

        else:  # n이 짝수인 경우
            if i == 0:  # d[0][0 ~ m - 1]인 경우 n * m - j를 리스트의 반복저장 (1씩 감소)
                k = n * m - j
                d[i][j] = k
            # d[짝수][0 ~ m - 1]인 경우 d[i - 1][m - 1] - m + j를 리스트에 반복 저장 (1씩 증가)
            elif i % 2 != 0:
                k = d[i - 1][m - 1] - m + j
                d[i][j] = k
            else:  # 나머지인 경우 d[i - 1][m - 1] - m - j를 리스트의 반복 저장 (1씩 감소)
                k = d[i - 1][m - 1] - m - j
                d[i][j] = k


for i in range(n):
    for j in range(m):
        print(d[i][j], end=' ')
    print()
