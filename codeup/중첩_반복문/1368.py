# 평행사변형 출력하기 2

h, k, d = input().split()   # h = 높이, k = 별의 개수, d = 방향
h = int(h)
k = int(k)
for i in range(h):

    if d == 'L':
        print(' '*i, end='')
    if d == 'R':
        print(' ' * (h - 1 - i), end='')

    for j in range(k):
        print('*', end='')
    print()
