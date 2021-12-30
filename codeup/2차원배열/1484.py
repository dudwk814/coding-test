n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y = 0, 0
t = 0
d[x][y] = 1


while t < n * m:
    if t % 4 == 0:  # 오른쪽으로 이동
        for i in range(m):
            ny = y + 1
            if ny < 0 or ny >= m:
                break

            if d[x][ny] == 0:  # 갈 수 있으면
                d[x][ny] = d[x][y] + 1
                y += 1
            else:
                break
    elif t % 4 == 1:  # 아래로 이동
        for i in range(n):
            nx = x + 1
            if nx < 0 or nx >= n:
                break

            if d[nx][y] == 0:  # 갈 수 있으면
                d[nx][y] = d[x][y] + 1
                x += 1
            else:
                break
    elif t % 4 == 2:  # 좌로 이동
        for i in range(m):
            ny = y - 1
            if ny < 0 or ny >= m:
                break

            if d[x][ny] == 0:  # 갈 수 있으면
                d[x][ny] = d[x][y] + 1
                y -= 1
            else:
                break
    elif t % 4 == 3:  # 위로 이동
        for i in range(m):
            nx = x - 1
            if nx < 0 or nx >= n:
                break

            if d[nx][y] == 0:  # 갈 수 있으면
                d[nx][y] = d[x][y] + 1
                x -= 1
            else:
                break
    t += 1


for i in range(n):
    for j in range(m):
        print(d[i][j], end=' ')
    print()
