# 종이 자르기
n, m = map(int, input().split())  # n = 가로, m = 세로

for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1:    # 세로가 처음이거나 끝일때
            if j == 0:    # 가로가 처음이거나 끝일때 즉 가로 세로 겹치는 부분
                print('+', end='')
            elif j == n - 1:
                print('+', end='')
                break
            else:
                print('-', end='')
        elif i != 0 or i != m - 1:  # 각 모서리가 아닌 중간 부분
            if j == 0:
                print('|', end='')
            elif j == n - 1:
                print('|', end='')
                break
            else:
                print(' ', end='')

    print()
