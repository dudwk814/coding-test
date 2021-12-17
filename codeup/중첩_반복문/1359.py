# 숫자 피라미드 1

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(j, end=' ')
    print()
