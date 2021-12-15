# 삼각형 출력하기3

n = int(input())

for i in range(n):
    for j in range(n):
        if i > j:
            print(' ', end='')
            continue
        print('*', end='')
    print()
