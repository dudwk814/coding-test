from collections import deque

m, n = map(int, input().split())

count = 0
zero_count = 0

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

print(*graph)


def bfs(x, y):

    global count

    queue = deque()

    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        count += 1

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_count += 1

if zero_count == 0:
    print(count)
else:
    print(-1)

print(* graph)
