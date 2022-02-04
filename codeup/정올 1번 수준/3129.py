input_data = input()

stack = []
status = True
for i in input_data:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) == 0:
            status = False
            break
        else:
            stack.pop()
if status and len(stack) == 0:
    print('good')
else:
    print('bad')
