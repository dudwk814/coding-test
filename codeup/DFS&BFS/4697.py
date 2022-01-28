import sys
sys.setrecursionlimit(1000000)
n = int(input())
array = []

count = 0
max_height = 0
for i in range(n):
    input_data = list(map(int, input().split()))
    max_height = max(max_height, max(input_data))
    array.append(input_data)

result = [0] * (max_height + 1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, h):

    # 주어진 범위를 넘어가면 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if array[x][y] <= h:
        return False

    if not visited[x][y]:
        visited[x][y] = True
        for i in range(4):
            dfs(x + dx[i], y + dy[i], h)
        return True


for i in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if dfs(j, k, i) == True:
                result[i] += 1

print(max(result))
