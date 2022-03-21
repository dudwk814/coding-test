import sys
sys.setrecursionlimit(20000)
t = int(input())


def dfs(x, y):

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


for i in range(t):
    count = 0
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())

        graph[y][x] = 1

    for i1 in range(n):
        for j1 in range(m):

            if dfs(i1, j1) == True:
                count += 1

    print(count)
