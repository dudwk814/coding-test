from audioop import avg


d = []

for i in range(5):
    d.append(int(input()))

d.sort()
print(int(sum(d) / 5))
print(d[2])
