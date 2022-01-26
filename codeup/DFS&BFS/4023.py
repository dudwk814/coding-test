# 맵 정보 입력받기
array = []
for i in range(19):
    array.append(list(map(int, input().split())))
count = 0  # 이어진 돌의 개수

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
visited = []


def dfs(x, y, color, direction):
    global count
    global visited
    # 주어진 범위를 벗어나면 종료
    if x < 0 or x > 18 or y < 0 or y > 18:
        # count = 5일때 맵을 넘어갔으면 승리 종료
        if count == 5:
            print(color)
            return
        count = 0
        visited.clear()
        return
    if count == 0:
        if direction <= 3:
            if x + (dx[direction + 4]) < 0 or x + (dx[direction + 4]) > 18 or y + (dy[direction + 4]) < 0 or y + (dy[direction + 4]) > 18:
                pass
            else:
                if array[x + (dx[direction + 4])][y + (dy[direction + 4])] == array[x][y]:
                    return
        else:
            if x + (dx[direction - 4]) < 0 or x + (dx[direction - 4]) > 18 or y + (dy[direction - 4]) < 0 or y + (dy[direction - 4]) > 18:
                pass
            else:

                if array[x + (dx[direction - 4])][y + (dy[direction - 4])] == array[x][y]:
                    return
    # 처음 돌색과 다르다면 종료
    if array[x][y] != color:
        # count = 5일때 현재 칸이 다른 색이면 승리 종료
        if count == 5:
            print(color)
            return
        count = 0
        visited.clear()
        return
    else:
        count += 1

    if count > 5:
        count = 0
        visited.clear()
        return

    visited.append((x, y))
    dfs(x + dx[direction], y + dy[direction], color, direction)


for i in range(19):
    for j in range(19):
        if array[i][j] == 1 or array[i][j] == 2:
            # 8방향 탐색
            for k in range(8):
                dfs(i, j, array[i][j], k)
                if count == 5:
                    if k == 0 or k == 4:
                        print(i + 1, j + 1)
                    else:
                        visited.sort(key=lambda key: key[1])
                        print(visited[0][0] + 1, visited[0][1] + 1)
                    break
            if count == 5:
                break
    if count == 5:
        break

if count != 5:
    print(0)
