from itertools import permutations

n, m = map(int, input().split())

d = []

for i in range(1, n + 1):
    d.append(i)

d = list(permutations(d, m))

for i in range(len(d)):
    for j in range(len(d[i])):
        print(d[i][j], end=' ')
    print()
