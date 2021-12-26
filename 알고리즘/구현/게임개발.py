# N, M 값 입력받기
n, m = map(int, input().split())

# 캐릭터가 방문한 좌표를 저장할 맵 생성
d = [[0] * m for _ in range(n)]

# 캐릭터의 현재 좌표 및 방향 설정
x, y, direction = map(int, input().split())

# 캐릭터의 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 리스트 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전 함수


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
coutn = 1
turn_time = 0
while True:
    # 왼쪽 회전
    turn_left()

    # 회전 방향으로 한칸 전진
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 전진한 칸이 갈 수 있는 칸이면 x,y에 dx, dy 저장
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        coutn += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없다면
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤로 갈 수없다면 break
        else:
            break
        turn_time = 0

print(coutn)
