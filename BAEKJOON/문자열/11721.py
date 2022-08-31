s = input()
idx = 0

for i in range(len(s)):

    if idx % 10 == 0 and i != 0:
        print()
        print(s[i], end='')
    else:
        print(s[i], end='')

    idx += 1
