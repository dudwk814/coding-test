n, k = map(int, input().split())
count = 0
for i in range(0, 2 ** n):
    bin_i = bin(i)[2:]

    if str(bin_i).count('1') == k:
        count += 1
print(count)
