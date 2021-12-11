a, d, n = map(int, input().split())

for i in range(0, n - 1):
    a += d
    if i == n - 2:
        print(a)
