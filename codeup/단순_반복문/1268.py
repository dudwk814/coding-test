# n개의 수 중 짝수의 개수
n = int(input())
d = list(map(int, input().split()))
s = 0

for i in range(n):
    if d[i] % 2 == 0:
        s += 1

print(s)
