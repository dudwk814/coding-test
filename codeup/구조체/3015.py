n, m = map(int, input().split())
d = []
for i in range(n):
    a, b = input().split()
    d.append((a, int(b), i))

d.sort(key=lambda x: (-x[1], x[2]))

for i in range(m):
    print(d[i][0])
