from collections import deque

# N, M을 공백으로 구분하여 입벽받음
n, m = map(int, input().split())

# 맵 정보를 2차원 리스트로 입력받음
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 탐색을 위한 4 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현


def bfs(x, y):
    # 큐 사용을 위해 deque 라이브러리 사용
    queue = deque()

    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 맵을 넘어가는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽(0)을 만난 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0, 0))
