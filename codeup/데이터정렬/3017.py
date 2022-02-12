n = int(input())
d = []

for i in range(n):
    a, b = map(int, input().split())
    c = i

    d.append([a, b, c])

d.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in d:
    print(i[2] + 1, i[0], i[1])
