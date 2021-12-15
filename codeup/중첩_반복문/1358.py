# 삼각형 출력하기 5
n = int(input())
loof = int(n / 2 + 1)
k = 1
for i in range(loof):
    print(' '*(loof-k), end='')
    for j in range(n):
        if i == j:
            print('*'*(i + j + 1), end='')
            break
    print()    
    k += 1
