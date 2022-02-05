n = int(input())
score = list(map(int, input().split()))

for i in range(len(score)):
    score[i] = [score[i], i]

score.sort(reverse=True)

for i in range(len(score)):
    if i == 0:
        score[i] = [score[i][0], score[i][1], i + 1]
    if i > 0:
        if score[i][0] == score[i - 1][0]:
            score[i] = [score[i][0], score[i][1], score[i - 1][2]]
        else:
            score[i] = [score[i][0], score[i][1], i + 1]

score.sort(key= lambda x : x[1])

for i in score:
    print(i[0], i [2])
