n = int(input())
d = list(map(int, input().split()))
m = 0

for i in range(n):
    if d[i] > m:
        m = d[i]

print(m)
