import sys
sys.setrecursionlimit(10000)

# m = 세로, n = 가로, k = 직사각형의 수
m, n, k = map(int, input().split())

array = [[0] * (n + 1) for _ in range(m + 1)]
result = []
for i in range(k):
    input_data = list(map(int, input().split()))
    for j in range(input_data[1], input_data[3] + 1):
        for k in range(input_data[0], input_data[2] + 1):
            array[j][k] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0


def dfs(x, y):
    global count
    if x < 0 or x > m or y < 0 or y > n:
        return False

    if not array[x][y] == 1:
        array[x][y] = 1
        count += 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

        return True


for i in range(m + 1):
    for j in range(n + 1):
        count = 0
        if dfs(i, j) == True:

            result.append(count)


result.sort()

for value in result:
    print(value, end=' ')
