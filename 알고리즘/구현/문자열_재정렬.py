s = input()
data = []
result = 0
for value in s:
    if value.isdigit():
        result += int(value)
    else:
        data.append(ord(value))

data.sort()

for i in data:
    print(chr(i), end='')

print(result)
