# n * m 의 배열
n, m = map(int, input().split())
d = []
for i in range(n):
    data = list(map(int, input().split()))

    data.sort()
    d.append(data[0])

d.sort()
print(d[n-1])
