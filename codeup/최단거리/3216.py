import heapq

# 무한을 의미하는 변수 초기화
INF = int(1e9)

# 노드의 수와 간선의 수
n, m = map(int, input().split())

# 그래프의 연결을 나타낼 리스트 생성
graph = [[] for _ in range(n + 1)]

# 최단거리 테이블 초기화(무한으로)
distance = [[INF] for _ in range(n + 1)]


# 입력받은 간선 정보를 정수로 변환
def convertInt(x):
    return int(ord(x) - ord('A') + 1)


for i in range(m):
    a, b, c = input().split()
    a = convertInt(a)
    b = convertInt(b)
    c = int(c)

    # 양방향 그래프에 맞게 비용 설정
    # a에서 b로 가는 비용이 c라는 의미
    graph[a].append((b, c))
    # b에서 a로 가는 비용이 c라는 의미
    graph[b].append((a, c))

start, end = input().split()
start, end = convertInt(start), convertInt(end)
# 다익스트라 정의


def dijkstra(start):
    q = []
    # start의 거리를 0으로 변경하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start][0] = 0

    while q:  # 큐가 빌때까지 반복
        dist, now = heapq.heappop(q)

        if distance[now][0] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]][0]:

                distance[i[0]] = [cost, now]
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 시작
dijkstra(start)
order = []


def dfs(array, end):
    if array[end][1] == start:
        order.append(array[end][1])

        return

    order.append(array[end][1])
    dfs(array, array[end][1])


if distance[end][0] == INF:
    print(-1)
else:
    order.append(end)
    if start != end:
        dfs(distance, end)

    print(distance[end][0])

    for i in range(len(order) - 1, -1, -1):
        print(chr(order[i] + ord('A') - 1))
