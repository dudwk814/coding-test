# 1의 개수 구하기 1번
n = int(input())
d = 0

for i in range(1, n + 1):
    if i % 10 == 1:
        d += 1

print(d)
