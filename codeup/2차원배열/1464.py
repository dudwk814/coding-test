# 2차원 배열 순서대로 채우기 1-5

n, m = map(int, input().split())
d = n * m
for i in range(n):
    for j in range(m):
        print(d, end=' ')
        d -= 1
    print()
