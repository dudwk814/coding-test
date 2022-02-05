n = int(input())
d = []
for i in range(n):
    a, b = map(int, input().split())
    d.append((a, b))

d.sort(key=lambda key: key[0])

for value in d:
    print(value[0], value[1])
