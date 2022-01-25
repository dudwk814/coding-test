# 처음의 맵 정보를 기록한 2차원 리스트
array1 = []
# 지뢰 찾기를 진행할 2차원 리스트
array2 = []
# 방문 정보를 저장할 2차원 리스트
visited = [[False] * 9 for _ in range(9)]

# 맵정보 채우기
for i in range(9):
    input_data = list(map(int, input().split()))
    array1.append(input_data)
    array2.append(input_data[:])

# 처음 클릭할 좌표
r, c = map(int, input().split())
# 리스트는 0부터 시작하므로 좌표 1씩 마이너스
r -= 1
c -= 1

# 8방향 이동 좌표 (시계 방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# dfs 알고리즘


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 종료
    if x < 0 or x >= 9 or y < 0 or y >= 9:
        return

    # x,y의 좌표가 지뢰라면 리턴
    if array1[x][y] == 1:
        return

    # 방문하지 않은 경우만 탐색
    if not visited[x][y]:

        visited[x][y] = True

        exist = False  # 8 방향 내에 지뢰 존재 여부
        count = 0  # 8방향중 지뢰가 아닌 곳이 존재한다면 1씩 증가, 즉 count >= 1 이면 방문처리
        # x,y의 좌표가 지뢰라면 리턴
        if array1[x][y] == 1:
            return
        # 8방향 탐색
        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 범위를 넘어가지 않는 경우만 탐색
            if nx >= 0 and nx < 9 and ny >= 0 and ny < 9:
                # array1[nx][ny]의 값이 1이라면 array2[x][y] 값을 1 증가
                if array1[nx][ny] == 1:
                    array2[x][y] += 1

        if array2[x][y] >= 1:
            return

        for i in range(8):
            dfs(x + dx[i], y + dy[i])


# dfs 수행
if array1[r][c] == 0:
    dfs(r, c)
    # 출력
    for i in range(9):
        for j in range(9):
            if visited[i][j] == True:
                print(array2[i][j], end=' ')
            else:
                print('_', end=' ')
        print()
else:
    for i in range(9):
        for j in range(9):
            if i == r and j == c:
                print(-1, end=' ')
            else:
                print('_', end=' ')
        print()
