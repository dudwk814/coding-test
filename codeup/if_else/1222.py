# 축구의 신 2

time, score1, score2 = map(int, input().split())

for i in range(time, 90):
    if i == time:
        score1 += 1
        continue
    if (i - time) % 5 == 0:  # 5분마다 1골씩 증가
        score1 += 1


if score1 > score2:
    print('win')
elif score1 == score2:
    print('same')
else:
    print('lose')
