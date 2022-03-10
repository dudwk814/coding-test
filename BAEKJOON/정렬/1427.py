input_data = input()
d = []
for i in input_data:
    d.append(int(i))

d.sort(reverse=True)

for i in d:
    print(i, end='')
