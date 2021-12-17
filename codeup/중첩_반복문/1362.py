# 숫자 피라미드 3

n = int(input())
d = 0
for i in range(1, n + 1):
    d += i

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(d, end=' ')
            d -= 1
    print()
