n = int(input())
score = []

for i in range(n):
    a, b, c = map(int, input().split())
    score.append((a, b, c))

score.sort(key=lambda score: -score[2])
d = []


count = 1
no = score[0][0]
for i in range(len(score)):
    if count == 3:
        if no == score[i][0]:
            continue
    if len(d) == 3:
        break
    if no == score[i][0]:
        count += 1
        d.append((score[i][0], score[i][1]))
    else:
        count = 1
        no = score[i][0]
        d.append((score[i][0], score[i][1]))

for score in d:
    print(score[0], score[1])
