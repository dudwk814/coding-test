n = int(input())

for i in range(0, (2 ** n)):
    bin_i = bin(i)[2:]

    if len(bin_i) < n:
        sub = n - len(bin_i)
        bin_i = ('0' * sub) + bin_i

    for j in bin_i:
        if j == '0':
            print('O', end='')
        else:
            print('X', end='')

    print()
