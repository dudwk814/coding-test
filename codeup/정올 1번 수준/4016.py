d = list(map(int, input().split()))
d.sort()
max_vlaue = 0

for i in range(1, d[0] + 1):
    if d[0] % i == 0 and d[1] % i == 0 and d[2] % i == 0:
        max_vlaue = max(max_vlaue, i)

print(max_vlaue)
