# 삼각형 출력하기2
n = int(input())

for i in range(n):
    for j in range(n - 1, -1, -1):
        print('*', end='')
        if i == j:
            break
    print()
