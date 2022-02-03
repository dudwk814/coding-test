input_data = input()

result = 10

for i in range(1, len(input_data)):
    if input_data[i - 1] == input_data[i]:
        result += 5
    else:
        result += 10

print(result)
