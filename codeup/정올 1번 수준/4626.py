count = 0
score = 0
n = int(input())
d = list(map(int, input().split()))

for i in range(n):
    if d[i] == 1:
        count += 1
        score += count
    else:
        count = 0
print(score)
