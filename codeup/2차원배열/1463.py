# 2차원 배열 순서대로 채우기 1-4

n = int(input())

for i in range(n, 0, -1):
    for j in range(n):
        print(i + (n * j), end=' ')
    print()
