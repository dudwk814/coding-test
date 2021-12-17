# 터널 통과하기 2

a, b, c = map(int, input().split())

list = [a, b, c]

for i in range(len(list)):
    if list[i] <= 170:
        print('CRASH', list[i], sep=' ')
        break
    if i == len(list) - 1 and list[i] > 170:
        print('PASS')
