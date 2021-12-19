# 2차원 배열 순서대로 채우기 1-7

n, m = map(int, input().split())

d = n * m

for i in range(n):

    for j in range(m):
        print(d - (n * j), end=' ')
    print()
    d -= 1
