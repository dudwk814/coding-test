
array = [[0] * 9 for _ in range(9)]
is_find = False
max_value = 0

for i in range(9):
    input_data = list(map(int, input().split()))
    for j in range(9):
        array[i][j] = input_data[j]
        max_value = max(max_value, input_data[j])

print(max_value)

for i in range(9):
    for j in range(9):
        if array[i][j] == max_value:
            print(i + 1, j + 1)
            is_find = True
            break
    if is_find:
        break
