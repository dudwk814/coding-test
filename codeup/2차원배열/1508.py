# 나도 IQ 150

n = int(input())
d = []
for i in range(n):
    d.append([])
    d[i].append(int(input()))

for i in range(n):
    for j in range(n):
        if i == 0:
            break
        if j == 0:
            continue
        if i < j:
            break

        k = d[i][j - 1] - d[i - 1][j - 1]
        d[i].append(k)

for i in range(n):
    for j in range(len(d[i])):
        print(d[i][j], end=' ')
    print()
