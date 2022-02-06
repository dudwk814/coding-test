n, k = map(int, input().split())
count = 0
data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

for value in data:
    if k // value >= 1:
        count += k // value
        k %= value
print(count)
