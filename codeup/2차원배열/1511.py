# 테두리의 합

n = int(input())
d = []
k = 0
r = 0
for i in range(n):
    d.append([])
    for j in range(n):
        d[i].append(0)

for i in range(n):
    for j in range(n):
        k += 1
        d[i][j] = k

        if i == 0 or i == n - 1:
            r += d[i][j]

        else:
            if j == 0 or j == n - 1:
                r += d[i][j]


print(r)
