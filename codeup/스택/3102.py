import re
stack = []
n = int(input())

for _ in range(n):
    commnad = input()

    if 'push' in commnad:
        num = re.findall("\d+", commnad)
        stack.append(num)
    elif 'top' in commnad:
        if len(stack) == 0:
            print(-1)
        else:
            print(*stack[len(stack) - 1])
    elif 'pop' in commnad:
        if len(stack) != 0:
            stack.pop()
    elif 'size' in commnad:
        print(len(stack))
    elif 'empty' in commnad:
        if len(stack) == 0:
            print("true")
        else:
            print("false")
