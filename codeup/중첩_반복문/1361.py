# 별 계단 만들기
n = int(input())

for i in range(n):
    if i != 0:
        print(' ' * i, end='')
    for j in range(2):
        print('*', end='')
    print()
