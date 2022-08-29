t = int(input())

for _ in range(t):
    n, w = input().split()
    n = int(n)

    for i in w:
        print(i * n, end='')
    print()
