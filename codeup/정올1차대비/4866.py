n, k = map(int, input().split())
student = [[0]*2 for _ in range(4)]
count = 0

for i in range(n):
    s, y = map(int, input().split())

    if y == 1 or y == 2:
        student[1][s] += 1
    elif y == 3 or y == 4:
        student[2][s] += 1
    else:
        student[3][s] += 1

for i in range(1, 4):
    if i == 1:
        p = student[i][0] + student[i][1]

        count += p // k
        if p % k != 0:
            count += 1
        continue
    for j in range(2):
        count += student[i][j] // k
        if student[i][j] % k != 0:
            count += 1
print(count)
