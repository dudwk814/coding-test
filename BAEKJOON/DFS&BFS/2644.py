import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
start, end = map(int, sys.stdin.readline().split())
m = int(input())

visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
result = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):

    for i in graph[v]:
        if not visited[i]:
            visited[i] += visited[v] + 1

            if i == end:
                break
            else:
                dfs(graph, i, visited)


dfs(graph, start, visited)
if visited[end] == 0:
    print(-1)
else:
    print(visited[end])
