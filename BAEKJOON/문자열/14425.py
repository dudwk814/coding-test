n, m = map(int, input().split())

array1 = []
array2 = []

for i in range(n):
    array1.append(input())

for i in range(m):
    array2.append(input())

count = 0

for i in array1:

    count += array2.count(i)

print(count)
