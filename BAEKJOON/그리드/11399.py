n = int(input())
d = [x for x in map(int, input().split())]
d.sort()

count = 0
for i in range(len(d)):
    count += d[i]
    d[i] = count

print(sum(d))
