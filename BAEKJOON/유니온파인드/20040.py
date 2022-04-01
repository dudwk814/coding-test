import sys
sys.setrecursionlimit(10**9)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())

parent = [0] * n

for i in range(n):
    parent[i] = i

cycle = False
result = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if cycle == False:
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            result = i + 1
        else:
            union_parent(parent, a, b)

if cycle == False:
    print(0)
else:
    print(result)
