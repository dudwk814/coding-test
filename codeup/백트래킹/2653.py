n = int(input())
count = 0

if n == 1:
    print(2)
elif n == 2:
    print(3)
else:
    for i in range(2 ** n):
        doubleling = False
        bin_i = bin(i)[2:]

        if len(bin_i) < n:
            sub = n - len(bin_i)
            bin_i = ('0' * sub) + bin_i

        for j in range(1, n):
            if bin_i[j] == '0' and bin_i[j - 1] == '0':
                doubleling = True
                break

        if not doubleling:
            count += 1
    print(count)
