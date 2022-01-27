import sys
sys.setrecursionlimit(10000)

# 맵 크기 정보 입력
n, m = map(int, input().split())
array1 = [[0] * m for _ in range(n)]
array2 = [[0] * m for _ in range(n)]

# 각각의 최소 조각횟수를 저장할 count
count1 = 0
count2 = 0

# 맵 정보 입력
for i in range(n):
    input_data = list(map(int, input().split()))

    for j in range(m):
        array1[i][j] = input_data[j]
        array2[i][j] = input_data[j]


# 4방향 탐색 정의 (동, 서, 남, 북)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# dfs 정의


def dfs(array, x, y, color1, color2):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if array[x][y] != color1:
        return False
    else:
        array[x][y] = color2
        for i in range(4):
            dfs(array, x + dx[i], y + dy[i], color1, color2)
        return True


# 켜기 최소 횟수 구하기
for i in range(n):
    for j in range(m):
        if dfs(array1, i, j, 0, 1) == True:
            count1 += 1
        if dfs(array2, i, j, 1, 0) == True:
            count2 += 1

print(count1, count2)
