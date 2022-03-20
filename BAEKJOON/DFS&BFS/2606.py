from collections import deque

v = int(input())
m = int(input())

graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
count = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start, visited):
    global count
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)
print(count)
