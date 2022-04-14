from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)


def bfs(graph, start, visited):

    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, sys.stdin.readline().split())
count = 0
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)
