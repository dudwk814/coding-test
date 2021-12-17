a, b = map(float, input().split())

list = []

for i in range(10):
    if i == 0:
        list.append(a + b)
    elif i == 2:
        list.append(a - b)
    elif i == 3:
        list.append(b - a)
    elif i == 4:
        list.append(a * b)
    elif i == 6:
        list.append(a / b)
    elif i == 7:
        list.append(b / a)
    elif i == 8:
        list.append(a**b)
    elif i == 9:
        list.append(b**a)


list.sort()

print("%.6f" % list[len(list) - 1])
