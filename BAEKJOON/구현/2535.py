n = int(input())

s = []
max_c = 0
for i in range(n):
    c, n, score = map(int, input().split())

    max_c = max(max_c, c)
    s.append((c, n, score))

s.sort(key=lambda x: -x[2])

score = [[0] for i in range(max_c)]

d = 0
for i in range(len(s)):
    idx = s[i][0] - 1

    if d == 3:
        break

    if score[idx][0] < 2:
        score[idx][0] += 1
        d += 1
        print(s[i][0], s[i][1])
