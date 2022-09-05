count = 0

array = []

for i in range(8):
    w = list(input())
    array.append(w)

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 and array[i][j] == 'F':
                count += 1
        else:
            if j % 2 != 0 and array[i][j] == 'F':
                count += 1


print(count)
