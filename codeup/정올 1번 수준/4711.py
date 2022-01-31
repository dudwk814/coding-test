max_value = 0
current_value = 0
for i in range(4):
    output_value, input_value = map(int, input().split())
    current_value -= output_value
    max_value = max(max_value, current_value)
    current_value += input_value
    max_value = max(max_value, current_value)

print(max_value)
