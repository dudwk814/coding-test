# 비교
n = int(input())

k = list(map(int, input().split()))

for i in range(n):
    print(i + 1, end='')
    print(':', end=' ')
    for j in range(n):
        if i == j:
            continue
        if k[i] < k[j]:
            print('<', end=' ')
        elif k[i] == k[j]:
            print('=', end=' ')
        else:
            print('>', end=' ')
    print()
