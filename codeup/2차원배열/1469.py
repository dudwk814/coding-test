# 2차원 배열 지그재그 채우기 2-2

n = int(input())

d = n
for i in range(n):
    if i % 2 == 0:
        if i != 0:
            d += n
        for j in range(n):

            print(d, end=' ')
            d -= 1
    else:
        d += n
        for j in range(n):
            d += 1
            print(d, end=' ')
    print()
