h, m = map(int, input().split())

if h == 0 and m < 45:
    h = 23

    m = m + 60 - 45
else:
    if m >= 45:
        m -= 45
    else:
        h -= 1
        m = m + 60 - 45

print(h, m)
