while True:
    try:
        s = input()

        l, u, n, r = 0, 0, 0, 0
        for i in s:
            if i == " ":
                r += 1
            elif ord('a') <= ord(i) <= ord('z'):
                l += 1
            elif ord('A') <= ord(i) <= ord('Z'):
                u += 1
            else:
                n += 1

        print(l, u, n, r)

        l, u, n, r = 0, 0, 0, 0

    except EOFError:
        break
