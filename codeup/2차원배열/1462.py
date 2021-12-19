# 2차원 배열 순서대로 채우기 1-3

n = int(input())

for i in range(1, n + 1):
    for j in range(n):
        print(i + (n * j), end=' ')
    print()
