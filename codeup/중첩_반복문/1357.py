# 삼각형 출력하기 4
n = int(input())
k = 1
for i in range(n * 2 - 1):
    if i < n:
        for j in range(n):
            if i == j:
                print('*', end='')
                break
            print('*', end='')
    else:
        print('*' * (n - k), end='')
        k += 1
    print()
