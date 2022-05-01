t = int(input())

for _ in range(t):
    input_data = input()
    value = 0
    result = 0
    for i in range(len(input_data)):

        if i == 0:
            if input_data[i] == 'O':
                value += 1
                result += value
                continue

        if input_data[i] == 'O':
            value += 1
            result += value
        else:
            value = 0

    print(result)
