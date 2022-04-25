import sys
sys.setrecursionlimit(300000)

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
result = 0

def dfs1(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == '-':
        graph[x][y] = '.'
        dfs1(x, y - 1)
        dfs1(x, y + 1)
        return True
    return False


def dfs2(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == '|':
        graph[x][y] = '.'
        dfs2(x - 1, y)
        dfs2(x + 1, y)
        return True
    return False

for i in range(n):
    for j in range(m):
        if graph[i][j] == '-':
            dfs1(i, j)
            result += 1
        elif graph[i][j] == '|':
            dfs2(i, j)
            result += 1


print(result)