data = input()
d = []
for i in range(len(data) - 1, -1, -1):
    d.append(data[i])

for value in d:
    print(value, end='')
