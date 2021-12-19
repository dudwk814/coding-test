# 숫자 로테이션

n = int(input())

list = list(map(int, input().split()))


for i in range(n):
    temp = list[0]
    for j in range(n):
        print(list[j], end=' ')

    for k in range(n):
        if k == 0:
            continue
        elif k < n:
            list[k - 1] = list[k]

        if k == n - 1:
            list[k] = temp

    print()
