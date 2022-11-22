from collections import deque


def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(maps[0]) or ny < 0 or ny >= len(maps):
                continue

            if maps[ny][nx] == 0:
                continue

            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))

    answer = maps[len(maps) - 1][len(maps[0]) - 1]

    if answer == 1:
        return - 1
    else:
        return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
