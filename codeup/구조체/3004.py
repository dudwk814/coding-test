n = int(input())

array = list(map(int, input().split()))

for i in range(len(array)):
    array[i] = [array[i], i]

array.sort()

for i in range(len(array)):
    array[i] = [array[i][0], array[i][1], i]

array.sort(key=lambda x: x[1])

for i in array:
    print(i[2], end=' ')
