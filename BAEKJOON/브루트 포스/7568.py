n = int(input())

frame = []

for i in range(n):
    a, b = map(int, input().split())
    frame.append([a, b])


for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            pass
        # 덩치가 작은 경우 rank를 1 올림
        if frame[i][0] < frame[j][0] and frame[i][1] < frame[j][1]:
            rank += 1

    frame[i] = [frame[i][0], frame[i][1], rank]

for value in frame:
    print(value[2], end=' ')
