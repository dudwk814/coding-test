input_data = list(input().split())
stack = []
result = 0
for i in input_data:
    if i != '*' and i != '+' and i != '-' and i != '/':
        stack.append(i)
