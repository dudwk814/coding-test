# 맵 크기 입력받기
n = int(input())
d = [[0] * n for _ in range(n)]

# 단지의 개수
count = 0

# 각 단지당 집의 수
house = 0
houses = []

# 4방향 탐색(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 맵 정보 입력받기
for i in range(n):
    input_data = input()
    for j in range(n):
        d[i][j] = int(input_data[j])

# dfs


def dfs(x, y):
    global house
    # 범위를 넘어간 경우 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if d[x][y] == 0:
        return False
    else:
        d[x][y] = 0
        house += 1

        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True


for i in range(n):
    for j in range(n):
        house = 0

        if dfs(i, j) == True:
            count += 1
            houses.append(house)

print(count)
houses.sort()
for i in range(len(houses)):
    print(houses[i])
