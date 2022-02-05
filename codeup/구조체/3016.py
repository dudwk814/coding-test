n = int(input())
score = []
array = []
for i in range(n):
    a, b, c, d = input().split()
    score.append((a, int(b), int(c), int(d)))

score.sort(key=lambda x: -x[1])
array.append(score[0][0])
array.append(score[0][1])
score.sort(key=lambda x: (-x[2], -x[1]))

for i in range(len(score)):
    if score[i][1] == array[1]:
        array.append(i + 1)
score.sort(key=lambda x: (-x[3], -x[1]))

for i in range(len(score)):
    if score[i][1] == array[1]:
        array.append(i + 1)

for i in range(len(array)):
    if i == 1:
        continue
    print(array[i], end=' ')
