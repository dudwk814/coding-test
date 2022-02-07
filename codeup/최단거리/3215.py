import heapq

# 무한 값 설정
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 입력받은 노드 정보 정수로 변환


def convertInt(x):
    return int(ord(x) - ord('A') + 1)


# 간선 정보 입력받기
for i in range(m):
    a, b, c = input().split()
    c = int(c)
    a = convertInt(a)
    b = convertInt(b)
    graph[a].append((b, c))
    graph[b].append((a, c))

# 시작 노드와 끝 노드 입력받기
start, end = input().split()
start = convertInt(start)
end = convertInt(end)

# 다익스트라 정의


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 이미 처리된적 있는 노드라면 무시(최소 거리 테이블에 더 작은 값이 저장되어 있는 경우 이미 처리되었다고 간주)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 입접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 시작
dijkstra(start)

# 결과 출력
if distance[end] != INF:
    print(distance[end])
else:
    print(-1)
