import sys
sys.setrecursionlimit(10 ** 9)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(x, y, graph):

    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(8):
            dfs(x + dx[i], y + dy[i], graph)
        return True
    return False


while True:
    w, h = map(int, sys.stdin.readline().split())
    result = 0
    if w == 0 and h == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if dfs(i, j, graph):
                result += 1

    print(result)
