d = []
for i in range(9):
    d.append(int(input()))

print(max(d))
for i in range(9):
    if max(d) == d[i]:
        print(i + 1)
