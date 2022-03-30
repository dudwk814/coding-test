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


n, m = map(int, sys.stdin.readline().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    o, a, b = map(int, sys.stdin.readline().split())

    # o가 0인 경우 합집합
    if o == 0:
        union_parent(parent, a, b)
    else:
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a == b:
            print("YES")
        else:
            print("NO")
