pastas = []
juice = []

for i in range(5):
    n = int(input())

    if i <= 2:
        pastas.append(n)
    else:
        juice.append(n)

pastas.sort()
juice.sort()

result = pastas[0] + juice[0] + (pastas[0] + juice[0]) / 10
print("%.1f" % result)
