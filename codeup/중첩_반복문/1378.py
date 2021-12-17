# 수열의 합

n = int(input())
d = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            d += j
print(d)
