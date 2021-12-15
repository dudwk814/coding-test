# 가로 세로 길이 n인 사각형을 출력
n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
