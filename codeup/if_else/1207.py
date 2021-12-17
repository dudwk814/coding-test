# 윷놀이

list = list(map(int, input().split()))

d = 0

for i in range(len(list)):
    if list[i] == 1:
        d += 1

if d == 0:
    print('모')
elif d == 1:
    print('도')
elif d == 2:
    print('개')
elif d == 3:
    print('걸')
elif d == 4:
    print('윷')
