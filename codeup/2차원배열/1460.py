# 2차원 배열 순서대로 채우기 1-1

n = int(input())
d = 0
for i in range(n):
    for j in range(n):
        d += 1
        print(d, end=' ')
    print()
