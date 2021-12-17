# 축구의 신 1

time, score = map(int, input().split())

for i in range(time, 90):
    if i == time:
        score += 1
        continue

    if (i - time) % 5 == 0:

        score += 1

print(score)
