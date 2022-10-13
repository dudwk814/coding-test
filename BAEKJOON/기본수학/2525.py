h, m = map(int, input().split())
t = int(input())

M = m + t

if M >= 60:

    m = M - ((M // 60) * 60)

    h = h + (M // 60)

    if h >= 24:

        h = h - 24

    print(h, m)
else:
    print(h, M)
