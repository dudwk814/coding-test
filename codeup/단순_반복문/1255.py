a, b = map(float, input().split())

if a == b:
    print(a)

if a < b:
    while a <= b:
        print(format(a, ".2f"), end=' ')
        a += 0.01
