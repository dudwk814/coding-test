# 평행사변형 출력하기 1

n = int(input())
k = 1
for i in range(n):
    print(' ' * (n - k), end='')
    for j in range(n):
        print('*', end='')
    print()
    k += 1
