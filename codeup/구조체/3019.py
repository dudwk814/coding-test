n = int(input())
array = []

for i in range(n):
    a, b, c, d = input().split()
    array.append((a, int(b), int(c), int(d)))

array.sort(key=lambda x: (x[1], x[2], x[3], x[0]))
for value in array:
    print(value[0])
