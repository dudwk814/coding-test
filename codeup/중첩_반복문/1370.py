# 지그재그 출력하기
h, r = map(int, input().split())
d = 1
for i in range(r):
    for j in range(h * 2 - 1):

        for k in range(h):
            if j == 0 or j == h * 2 - 2:
                print('*', end='')
                break
            elif j < h:
                print(' '*j, end='')
                print('*', end='')
                break
            elif j == h:
                print(' '*(h - d - 1), end='')
                print('*', end='')
                d += 1
                break
            elif j > h:
                d += 1
                print(' ' * (h - d), end='')
                print('*', end='')
                break
        print()
    d = 1
