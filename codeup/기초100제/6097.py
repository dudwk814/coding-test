h, w = map(int, input().split())
n = int(input())

list = []

for i in range(h):
    list.append([])
    for j in range(w):
        list[i].append(0)


for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):  # 막대의 길이 만큼 반복
        if d == 0:  # 막대의 방향이 가로라면
            # 리스트는 0번부터지만 x, y 값은 1번부터이므로 -1씩해서 순서를 맞춤
            list[x - 1][(y + j) - 1] = 1
            # 방향에 따라 다음 좌표에 1을 저장
        else:
            list[(x + j) - 1][y - 1] = 1


for i in range(h):
    for j in range(w):
        print(list[i][j], end=' ')
    print()
