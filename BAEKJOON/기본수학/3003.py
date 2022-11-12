array = [1, 1, 2, 2, 2, 8]

array2 = list(map(int, input().split()))

for i in range(6):
    print(array[i] - array2[i], end=' ')
