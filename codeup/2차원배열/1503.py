# 지그재그 입력(2차원 배열)
n = int(input())
k = 0

for i in range(n):
    for j in range(n):
        if i == 0:
            k += 1
            print(k, end=' ')
        elif i % 2 != 0:
            if j == 0:
                k += n
                print(k, end=' ')
            else:
                k -= 1
                print(k, end=' ')
        else:
            if j == 0:
                k += n
                print(k, end=' ')
            else:
                k += 1
                print(k, end=' ')
    print()
