# 2차원 배열 채우기 4(역달팽이 배열)

# n * n 크기의 배열을 만들기 위한 n을 입력받음
n = int(input())

# 시작 위치 지정
x, y = 0, 0

# 몇 회째 루프인지
t = 1
# n * n 의 2차원 배열을 초기화
d = [[0] * n for _ in range(n)]

# 시작 위치 값 지정
d[x][y] = 1

while True:

    if t > n * n:
        break

    if t % 4 == 1:  # 아래로 이동
        for i in range(n):
            for i in range(n):
                nx = x + 1

                # 벽이면
                if nx < 0 or nx >= n:
                    break

                # 갈 수 있다면
                if d[nx][y] == 0:
                    d[nx][y] = d[x][y] + 1
                    x += 1
                else:
                    break
    elif t % 4 == 2:  # 오른쪽으로 이동
        for i in range(n):
            ny = y + 1

            # 벽이면
            if ny < 0 or ny >= n:
                break

            # 갈 수 있으면
            if d[x][ny] == 0:
                d[x][ny] = d[x][y] + 1
                y += 1
            else:
                break
    elif t % 4 == 3:  # 위로 이동
        for i in range(n):
            nx = x - 1

            # 벽이면
            if nx < 0 or nx >= n:
                break

            # 갈 수 있다면
            if d[nx][y] == 0:
                d[nx][y] = d[x][y] + 1
                x -= 1
            else:
                break
    else:
        for i in range(n):
            ny = y - 1

           # 벽이면
            if ny < 0 or ny >= n:
                break

            # 갈 수 있으면
            if d[x][ny] == 0:
                d[x][ny] = d[x][y] + 1
                y -= 1
            else:
                break

    t += 1


for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print()
