input_data = map(int, input().split())

result = 0

for i in input_data:
    result += i * i

print(result % 10)
