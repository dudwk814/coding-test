# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())

# 전체 맵 정보를 리스트로 받음 (2차원 리스트)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문처리
def dfs(x, y):

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 파라미터로 입력받은 좌표가 아직 방문하지 않은 노드라면 방문처리
    if graph[x][y] == 0:
        graph[x][y] = 1

        # 상, 하, 좌, 우 네 방향 모두 dfs 메서드를 이용해서 빈 노드를 탐색
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우

        return True  # 현재 방문 좌표의 값이 0이면 True
    return False    # 현재 방문 좌표의 값이 1이면 패스


result = 0  # 아이스크림이 될 수 있는 횟수

# 모든 노드를 돌면서 dfs를 수행하고 리턴 값이 True라면 Result값 증가
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)
