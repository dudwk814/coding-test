n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

result = sorted(d, reverse=True)
print(*result)
