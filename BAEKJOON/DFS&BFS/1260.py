from collections import deque

n, m, v = map(int, input().split())  # 노드의 개수 n, 간선의 개수 m, 시작 노드 v

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True

    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):

    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 출력
        v = queue.popleft()

        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


for i in range(1, n + 1):
    graph[i].sort()

for i in range(2):

    visited = [False] * (n + 1)

    if i == 0:
        dfs(graph, v, visited)
        print()
    else:
        bfs(graph, v, visited)
