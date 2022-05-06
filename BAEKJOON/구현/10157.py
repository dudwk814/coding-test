import sys

c, r = map(int, input().split())
target = int(input())

graph = [[0] * c for _ in range(r)]
x, y = r - 1, 0

graph[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
t_x = 1
t_y = 1
direction = 0
is_success = False

if target == 1:
    print(t_y, t_x)
else:
    while True:

        nx = x + dx[direction % 4]
        ny = y + dy[direction % 4]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue

        if graph[nx][ny] != 0:
            direction += 1
            continue

        graph[nx][ny] = graph[x][y] + 1

        if direction % 4 == 0:
            t_x += 1
        elif direction % 4 == 1:
            t_y += 1
        elif direction % 4 == 2:
            t_x -= 1
        else:
            t_y -= 1

        if graph[nx][ny] == target:
            is_success = True
            break

        x = nx
        y = ny

        if graph[x][y] == r * c:
            break
    if is_success:
        print(t_y, t_x)
    else:
        print(0)
