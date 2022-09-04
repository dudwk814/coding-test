while True:
    n = input()

    if n == '0':
        break
    r = n[::-1]

    n = int(n)
    r = int(r)

    if n == r:
        print("yes")
    else:
        print("no")
