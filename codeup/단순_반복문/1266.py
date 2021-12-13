# n개의 수의 합
n = int(input())
d = list(map(int, input().split()))
s = 0

for i in range(n):
    s += d[i]

print(s)
