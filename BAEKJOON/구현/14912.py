n, d = map(int, input().split())

frequency = 0

for i in range(1, n + 1):
    str_i = str(i)
    str_d = str(d)

    for j in str_i:
        if str_d in j:
            frequency += 1

print(frequency)
