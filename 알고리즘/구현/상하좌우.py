# n = int(input())
# data = input().split()
# d = []
# x, y = 0, 0
# for i in range(n):
#     d.append([])
#     for j in range(n):
#         d[i].append(j + 1)

# for i in range(len(data)):

#     if data[i] == 'R':  # 오른쪽으로 이동하는 경우
#         if y == 4:
#             continue
#         else:
#             y += 1
#     elif data[i] == 'L':  # 왼쪽으로 이동하는 경우
#         if y == 0:
#             continue
#         else:
#             y -= 1
#     elif data[i] == 'U':  # 위로 이동하는 경우
#         if x == 0:
#             continue
#         else:
#             x -= 1
#     elif data[i] == 'D':  # 아래로 이동하는 경우
#         if x == 4:
#             continue
#         else:
#             x += 1

# print(x + 1, y + 1)

# 답안
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:

    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
