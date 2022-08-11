s = []

for i in range(8):
    n = int(input())

    s.append((i + 1, n))

s.sort(key=lambda x: -x[1])
d = []
score = 0
for i in range(5):
    score += s[i][1]
    d.append(s[i][0])

d.sort()

print(score)
print(*d)
