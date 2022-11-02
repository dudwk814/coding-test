array = list(map(int, input().split()))

value = 0

for i in array:
    value += i * i

print(value % 10)
