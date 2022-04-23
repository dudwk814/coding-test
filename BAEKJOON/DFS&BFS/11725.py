import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):

    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(graph, i, visited)


dfs(graph, 1, visited)

for i in range(2, len(visited)):
    print(visited[i])
