idx = 0
max_value = 0
for i in range(1, 10):
    n = int(input())

    if n > max_value:
        max_value = n
        idx = i
print(max_value)
print(idx)
