from types import coroutine


data = input()
result = 0

for value in data:
    value = int(value)

    if result == 0:
        result += value
        continue

    if value == 0 and  value == 1:
        result += value
    else:
        result *= value

print(result)
