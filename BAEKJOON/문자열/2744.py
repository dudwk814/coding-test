s = input()

for i in s:

    if ord('a') <= ord(i) <= ord('z'):
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')
