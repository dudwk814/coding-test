n = int(input())
count = 0

array = [[0] * 100 for _ in range(100)]

for i in range(n):
    a1, b1 = map(int, input().split())
    a1 -= 1
    b1 -= 1

    a2, b2 = a1 + 10, b1 + 10

    for j in range(b1, b2):
        for k in range(a1, a2):
            array[j][k] = 1

for i in range(100):
    for j in range(100):
        if array[i][j] == 1:
            count += 1

print(count)
