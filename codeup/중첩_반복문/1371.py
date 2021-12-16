# 마름모 출력하기

n = int(input())
d = 0
for i in range(1, (n * 2 + 1)):
    if i <= n:
        for j in range(1, (n * 2 + 1)):

            print(' '*(n - i), end='')
            print('*', end='')
            print(' '*((i-1)*2), end='')
            d = ((i-1)*2)
            print('*', end='')
            break

        print()
    else:
        for j in range(1, (n * 2 + 1)):
            print(' '*(i - (n + 1)), end='')
            print('*', end='')
            print(' '*d, end='')
            d -= 2
            print('*', end='')
            break
        print()
