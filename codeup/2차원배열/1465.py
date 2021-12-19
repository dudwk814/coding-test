# 2차원 배열 순서대로 채우기 1-6

n, m = map(int, input().split())
d = n * m
for i in range(n):
    if i == 0:
        d -= m - 1
    else:
        d -= m
    for j in range(m):
        print(d + j, end=' ')
    print()
