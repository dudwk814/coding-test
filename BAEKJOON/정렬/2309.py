d = []
for i in range(9):
    d.append(int(input()))

sum_value = sum(d)
d.sort()
target = sum_value - 100

is_find = False

for i in range(len(d)):

    for j in range(len(d)):

        value1 = d[i]
        value2 = d[j]

        if i == j:
            continue
        if target == value1 + value2:

            d.remove(value1)
            d.remove(value2)

            is_find = True
            break
    if is_find:
        break

for i in d:
    print(i)
