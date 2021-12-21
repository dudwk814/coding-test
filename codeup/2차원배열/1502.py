# 2차원 배열 채우기 2

n = int(input())
k = 0
for i in range(n):
    for j in range(n):
        if j == 0:
            k = i + 1
            print(k, end=' ')
        else:
            k += n
            print(k, end=' ')
    print()
