import sys
sys.setrecursionlimit(10 ** 9)

t = int(input())


def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == '#':
        graph[x][y] = '.'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for _ in range(t):
    h, w = map(int, input().split())
    result = 0
    graph = [list(input()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                dfs(i, j)
                result += 1

    print(result)
