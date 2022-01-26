# 맵 정보 입력받기
array = [[] * 10 for _ in range(10)]
for i in range(10):
    input_data = list(input())
    for j in range(len(input_data)):
        array[i].append(input_data[j])

# 색채우기를 할 좌표
x, y = map(int, input().split())
# 4방향 진행 테이블 (동, 서, 남, 북)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(x, y):

    if x < 0 or x > 9 or y < 0 or y > 9:
        return
    # 현재 좌표 값이 '*'인 경우 종료
    if array[y][x] == '*':
        return
    else:  # 아니라면 현재 좌표 값을 '*'으로 변경
        array[y][x] = '*'

    for i in range(4):
        dfs(x + dx[i], y + dy[i])


dfs(x, y)

# 출력
for i in range(10):
    for j in range(10):
        print(array[i][j], end='')
    print()
