v = int(input())  # 노드의 수
e = int(input())  # 간선의 수

# 그래프 초기화
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 처리를 위한 테이블
visited = [False] * (v + 1)

# 바이러스의 걸리는 컴퓨터의 수
count = 0

# dfs


def dfs(graph, v, visited):
    global count
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(count)
