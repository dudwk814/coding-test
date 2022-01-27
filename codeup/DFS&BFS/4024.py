import sys
sys.setrecursionlimit(10000)
w, h = map(int, input().split())  # 맵의 넓이, 높이

# 호수의 개수
count = 0
# 맵 입력받기
array = [[] * w for _ in range(h)]
for i in range(h):
    input_data = input().split()
    for value in input_data:
        array[i].append(value)


# 8방향 탐색 (시계방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# dfs 정의


def dfs(x, y):
    # 범위를 넘어간 경우 종료
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    # 현재 좌표가 강(L)이 아닌경우 종료
    if array[x][y] != 'L':
        return False

    # 현재 좌표가 강이라면 .으로 변경후 8 방향 탐색
    else:
        array[x][y] = '.'
        for i in range(8):
            dfs(x + dx[i], y + dy[i])
        return True


for i in range(h):
    for j in range(w):
        if dfs(i, j):
            count += 1

print(count)
