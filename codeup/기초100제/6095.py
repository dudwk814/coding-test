d = []  # 바둑판이 될 리스트
for i in range(20):
    d.append([])    # 2중 리스트로 만들기

    for j in range(20):
        d[i].append(0)  # 2중 리스트의 값들을 0으로 전부 초기화

n = int(input())  # 흰 돌의 개수

for i in range(n):
    x, y = map(int, input().split())  # n만큼 흰돌의 좌표를 입력
    d[x][y] = 1

for i in range(1, 20):  # x, y의 좌표는 1부터 시작이므로 루프를 1부터 19까지 돌림
    for j in range(1, 20):  # 2중 리스트이므로 2중 루프 사용
        print(d[i][j], end=' ')
    print()
