d = []  # 바둑판이 될 리스트

for i in range(20):
    d.append([])    # 바둑판을 2중 리스트로 만듬
    for j in range(20):
        d[i].append(0)      # 바둑판의 좌표를 0으로 초기화

for i in range(19):
    a = input().split()  # 바둑판 한줄의 값들을 입력
    for j in range(19):
        d[i + 1][j + 1] = int(a[j])  # 입력받은 값들을 바둑판 좌표에 저장

n = int(input())    # 10자 뒤집기의 횟수 입력

for i in range(n):  # 10자 뒤집기 회수만큼 반복
    x, y = map(int, input().split())    # 뒤집을 좌표 입력
    for j in range(1, 20):
        if d[j][y] == 0:    # [j][y]좌표가 0이라면 1로 바꾸고 1이라면 0으로 변경
            d[j][y] = 1
        else:
            d[j][y] = 0

        if d[x][j] == 0:    # [x][j]좌표가 0이라면 1로 바꾸고 1이라면 0으로 변경
            d[x][j] = 1
        else:
            d[x][j] = 0

for i in range(1, 20):  # 출력
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
