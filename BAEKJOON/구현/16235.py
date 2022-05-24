from collections import deque

n, m, k = map(int, input().split(' '))

a = [list(map(int, input().split(' '))) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
trees = deque()  # 나무들이 들어있는 deque
dead_trees = list()
for _ in range(m):
    x, y, z = map(int, input().split(' '))
    trees.append([z, x, y])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def spring_summer():
    len_ = len(trees)
    for _ in range(len_):
        z, x, y = trees.popleft()
        if graph[x - 1][y - 1] < z:
            dead_trees.append([z, x, y])
        else:
            graph[x - 1][y - 1] -= z
            trees.append([z + 1, x, y])

    while dead_trees:
        z, x, y = dead_trees.pop()
        graph[x - 1][y - 1] += z // 2


def fall_winter():
    for z, x, y in list(trees):
        if z % 5 == 0:
            for i in range(8):
                nx, ny = x + dx[i] - 1, y + dy[i] - 1

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                trees.appendleft([1, nx + 1, ny + 1])

    for i in range(n):
        for j in range(n):
            graph[i][j] += a[i][j]


for i in range(k):
    spring_summer()
    fall_winter()

print(len(trees))
