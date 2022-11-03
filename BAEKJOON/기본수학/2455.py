max_value = 0
value = 0

for i in range(4):
    a, b = map(int, input().split())
    value -= a
    value += b
    max_value = max(max_value, value)

print(max_value)
