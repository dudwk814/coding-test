# 사각형 출력하기 3
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:
            print('*'*n, end='')
            break

        if j == 0 or j == n - 1:
            print('*', end='')
        elif j == i:
            print('*', end='')
        elif j == n - 1 - i:
            print('*', end='')
        else:
            print(' ', end='')

    print()
