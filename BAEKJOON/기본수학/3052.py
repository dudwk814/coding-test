array = []

for i in range(10):
    n = int(input())

    m = n % 42

    if m not in array:
        array.append(m)

print(len(array))
