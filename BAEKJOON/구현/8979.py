import sys

n, k = map(int, input().split())
s = []
score = []
for i in range(n):

    num, g, si, b = map(int, sys.stdin.readline().split())

    s.append((g, si, b))

    if num == k:
        score.append((g, si, b))


s.sort(key=lambda x: (-x[0], -x[1], -x[2]))

# print(s)
# print(s[0][0], s[0][1], s[0][2])

for i in range(len(s)):
    if score[0][0] == s[i][0] and score[0][1] == s[i][1] and score[0][2] == s[i][2]:
        print(i + 1)
        break
