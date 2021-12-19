# 2차원 배열 순서대로 채우기 1-8
n, m = map(int, input().split())

d = (n * m) - (n - 1)

for i in range(n):

    for j in range(m):
        print(d - (n * j), end=' ')
    print()
    d += 1
