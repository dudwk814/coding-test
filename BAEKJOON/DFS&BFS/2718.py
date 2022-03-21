from collections import deque

n, m = map(int, input().split())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 맵을 넘어가면 continue
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽(0)을 만나면 패스
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs(0, 0)

print(graph[n - 1][m - 1])
