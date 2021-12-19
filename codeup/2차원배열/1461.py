# 2차원 배열 순서대로 채우기 1-2
n = int(input())

for i in range(1, n + 1):
    d = n * i
    for j in range(n):
        print(d, end=' ')
        d -= 1
    print()
