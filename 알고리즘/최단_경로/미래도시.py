# 도달할 수 없는 무한의 거리인 경우 -1
INF = int(1e9)

# 회사의 개수 = n, 경로의 개수 = m
n,m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 도착해야 하는 노드 x, k를 입력받음
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for c in range(1, n + 1): # 환승 노드
    for a in range(1, n + 1): # 출발 노드
        for b in range(1, n + 1): # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

distance = graph[1][k] + graph[k][x]
if distance == INF:
    print("-1")
else:
    print(distance)    


