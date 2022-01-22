a, b = map(int, input().split())
min_value = min(a, b)
max_value = max(a, b)
result = 0
if a == b:
    print(a)
else:
    for i in range(1, min_value + 1):
        if min_value % i == 0:
            if max_value % i == 0:
                result = i
    print(result)
