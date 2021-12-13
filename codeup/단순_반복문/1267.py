# n개의 수 중 5의 배수의 합
n = int(input())
d = list(map(int, input().split()))
s = 0

for i in range(n):
    if d[i] % 5 == 0:
        s += d[i]

print(s)
