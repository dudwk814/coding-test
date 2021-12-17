# 삼각형의 성립 조건

list = list(map(int, input().split()))

list.sort()

if list[2] < list[0] + list[1]:
    print('yes')
else:
    print('no')
