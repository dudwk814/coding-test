# 칼로리 계산하기
d = list(map(int, input().split()))
list = [400, 340, 170, 100, 70]
kcal = 0

for i in range(len(d)):
    for j in range(1, 6):
        if d[i] == j:
            kcal += list[j - 1]

if kcal > 500:
    print('angry')
else:
    print('no angry')
