s = input()

for i in s:
    w = ord(i)

    if ord('a') <= w <= ord('z'):
        w += 13

        if w > ord('z'):
            w = (w - ord('z')) + (ord('a') - 1)
    elif ord('A') <= w <= ord('Z'):
        w += 13

        if w > ord('Z'):
            w = (w - ord('Z')) + (ord('A') - 1)

    print(chr(w), end='')
