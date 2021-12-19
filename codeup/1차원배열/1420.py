# 3등 찾기

n = int(input())
people = []
score = []
list = []
for i in range(n):
    a, b = input().split()

    people.append(a)
    score.append(int(b))
    list.append(a)
    list.append(int(b))

score.sort()

result = list.index(score[len(score) - 3])

print(list[result - 1])
