import sys
sys.setrecursionlimit(10 ** 9)

# 특정 원소가 속한 집합을 찾기


def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):
    array = list(map(int, sys.stdin.readline().split()))

    for j in range(n):

        if array[j] == 1:
            union_parent(parent, i, j + 1)

plan = list(map(int, sys.stdin.readline().split()))
result = True
for i in range(1, m):
    a = find_parent(parent, plan[0])
    b = find_parent(parent, plan[i])

    if a != b:
        result = False
        break

if result:
    print("YES")
else:
    print("NO")
