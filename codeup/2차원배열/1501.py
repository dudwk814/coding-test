# 2차원 배열 채우기 1

n = int(input())
k = 0

for i in range(n):
    for j in range(n):
        k += 1
        print(k, end=' ')
    print()
