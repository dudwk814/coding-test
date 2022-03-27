import sys
import heapq

inf = float('inf')

n, e = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]


for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start):

    distance = [inf] * (n + 1)
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:

                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


d_start = dijkstra(1)
d_v1 = dijkstra(v1)
d_v2 = dijkstra(v2)

answer = min(d_start[v1] + d_v1[v2] + d_v2[n],
             d_start[v2] + d_v2[v1] + d_v1[n])

print(answer if answer != inf else -1)
