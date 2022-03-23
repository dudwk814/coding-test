from itertools import combinations_with_replacement
n, m = map(int, input().split())

d = [i for i in range(1, n + 1)]
d = list(combinations_with_replacement(d, m))

for i in range(len(d)):
    for j in range(len(d[i])):
        print(d[i][j], end=' ')
    print()
