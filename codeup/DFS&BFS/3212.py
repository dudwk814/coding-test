from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())

# 진입차수를 담을 리스트를 0으로 초기화
indegree = [0] * (v + 1)

# 노드에 연결된 간선을 관리하기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 모든 간선에 대한 정보 입력 받기
for i in range(e):
    a, b = map(int, input().split())  # 노드 A에서 B로 이동 가능
    graph[a].append(b)  # 간선 정보 설정
    indegree[b] += 1  # 진입차수 1 증가

# 위상 정렬 알고리즘


def topology_sort():
    result = []  # 위상 정렬 수행 결과를 담을 리스트
    q = deque()
    priority = 1e9

    # 첫 단계는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:

        for i in q:
            priority = min(priority, i)

        now = q.popleft()  # 큐에서 원소 pop
        result.append(now)  # 결과 리스트에 삽입

        # 현재 노드와 연결된 노드에 간선을 끊고 진입차수가 0이라면 큐에 삽입
        for i in graph[now]:
            indegree[i] -= 1  # 진입차수 1 감소

            if indegree[i] == 0:  # 진입차수가 0이라면 큐에 삽입
                q.append(i)

    if len(result) == v:
        # 결과 출력
        for i in result:
            print(i)
    else:
        print(-1)


topology_sort()
