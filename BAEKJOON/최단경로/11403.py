n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
