n = int(input())

graph = []
count = 0
house_count = 0
d = []


for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):

    global house_count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 현제 노드를 아직 방문하지 않았다면 방문처리
    if graph[x][y] == 1:
        graph[x][y] = 2
        house_count += 1

        # 상하좌우로 dfs 실행
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count += 1
            d.append(house_count)
            house_count = 0

print(count)

d.sort()

for value in d:
    print(value)
