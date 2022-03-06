a, b, c = map(int, input().split())
min_value = min(a, b, c)

result = 0


def find_divisor(i):
    if a % i == 0 and b % i == 0 and c % i == 0:
        return True
    else:
        return False


for i in range(1, min_value + 1):
    if find_divisor(i):
        result = i

print(result)
