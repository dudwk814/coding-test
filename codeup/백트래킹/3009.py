n, s = map(int, input().split())
input_data = list(map(int, input().split()))

count = 0
for i in range(2 ** n):
    bin_i = bin(i)[2:].zfill(n)
    sum = 0
    k = 0
    for j in range(len(bin_i)):
        if bin_i[j] == '1':
            sum += input_data[j]
            k += 1

    if sum == s and k:
        count += 1
print(count)
