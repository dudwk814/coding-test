d = []

for i in range(10):
    d.append([])
    for j in range(10):
        d[i].append(0)

# for i in range(10):
#     for j in range(10):
#         if i == 0 or i == 9:
#             d[i][j] = 1
#         if j == 0 or j == 9:
#             d[i][j] = 1

for i in range(10):
    a = input().split()
    for j in range(10):
        d[i][j] = int(a[j])
a = 1   # 시작 위치, 개미가 이동하다가 벽에 막히면 현재 좌표를 저장할 변수
b = 0   # 개미가 2에 도착하면 b에 2를 저장하고 반복 중지

for i in range(1, 9):
    if b == 2:  # 개미가 2에 도착했을경우
        break
    for j in range(1, 9):

        if a != j:  # a값과 j좌표가 맞을때까지 continue
            continue

        if d[i][j] == 0:    # 현재 좌표의 값이 0인 경우
            if d[i][j + 1] == 0:    # 다음 j좌표 값이 0인경우 현재 좌표의 값을 9로 변경하고 a의 값을 1 증가
                d[i][j] = 9
                a += 1
            # 다음 j좌표 값이 1(벽)인 경우 현재 좌표의 값을 9로 변경하고 a에 j값을 저장하고 2중 루프 벗어남
            elif d[i][j + 1] == 1:
                d[i][j] = 9
                a = j
                break
            # 다음 j좌표 값이 2(먹이)인 경우 현재 좌표의 값을 9로 변경하고 a에 값을 1 증가
            elif d[i][j + 1] == 2:
                d[i][j] = 9
                a += 1
        if d[i][j] == 2:    # 개미가 먹이에 도달한 경우 현재 좌표 값을 9로 변경하고 b에 2저장 후 루프 벗어남
            d[i][j] = 9
            b = 2
            break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
