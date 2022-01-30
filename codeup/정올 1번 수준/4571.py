d = []
m = int(input())
n = int(input())


for i in range(m, n + 1):
    for j in range(1, 101):
        if j * j == i:
            d.append(i)
print(sum(d))
print(min(d))
