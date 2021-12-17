# 숫자 피라미드 2

n = int(input())

for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if j <= i:
            print(i, end=' ')
    print()
