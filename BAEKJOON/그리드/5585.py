n = 1000 - int(input())
result = 0

values = [500, 100, 50, 10, 5, 1]

for value in values:

    if n // value >= 1:
        result += n // value
        n %= value

print(result)
