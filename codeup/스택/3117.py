k = int(input())
d = []

for i in range(k):
    a = int(input())

    if a == 0:
        d.pop()
    else:
        d.append(a)

print(sum(d))
