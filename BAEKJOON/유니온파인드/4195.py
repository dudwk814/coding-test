from re import A
import sys

sys.setrecursionlimit(10 ** 9)

t = int(sys.stdin.readline())

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

    if a != b:
        parent[b] = a
        number[a] += number[b]


for i in range(t):
    f = int(sys.stdin.readline())

    parent = dict()
    number = dict()

    for j in range(f):
        a, b = sys.stdin.readline().split()

        if a not in parent:
            parent[a] = a
            number[a] = 1

        if b not in parent:
            parent[b] = b
            number[b] = 1

        union_parent(parent, a, b)

        print(number[find_parent(parent, a)])
