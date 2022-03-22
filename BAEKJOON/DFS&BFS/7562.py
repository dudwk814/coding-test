from collections import deque
t = int(input())

step = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
count = []


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:

        x, y = queue.popleft()

        for i in range(8):
            nx = x + step[i][0]
            ny = y + step[i][1]

            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for i in range(t):
    l = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    graph = [[0] * l for _ in range(l)]

    bfs(x, y)

    if x == target_x and y == target_y:
        print(0)
    else:
        print(graph[target_x][target_y])
