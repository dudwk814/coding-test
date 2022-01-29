n = int(input())
m = int(input())

for i in range(2, n + 1):
    if i + (n - i) == n:
        if i - (n - i) == m:
            print(i)
            print((n - i))
