# 자리 배치
n, c = map(int, input().split())
h = list(map(int, input().split()))
h.sort()


for i in range(n):
    if i % c == 0 and i != 0:
        print()
    print(h[i], end=' ')
