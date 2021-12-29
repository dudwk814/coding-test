# 맵 정보 입력 받기
graph = []
for i in range(7):
    graph.append(list(map(int, input().split())))

# 방문한 위치를 저장하기 위한 2차원 리스트
d = [[0] * 7 for _ in range(7)]

# 같은 색이 3이상인 칸들의 개수
count = 0

# 탐색을 위한 4방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# DFS로 특정 노드를 방문한 뒤에 연결된 모든 노드 방문


def dfs(x, y):
    count = 1
    d[x][y] = 1

    current = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx <= 6 and ny >= 0 and ny <= 6:
            if d[nx][ny] == 0 and current == graph[nx][ny]:
                count += dfs(nx, ny)

    return count


for i in range(7):
    for j in range(7):
        if dfs(i, j) >= 3:
            count += 1

print(count)
