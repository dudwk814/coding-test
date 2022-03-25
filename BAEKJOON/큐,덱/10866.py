from collections import deque
import sys

n = int(input())
queue = deque()
for i in range(n):
    input_data = sys.stdin.readline()

    if "push_b" in input_data:
        oper, value = input_data.split()
        queue.append(int(value))

    elif "push_f" in input_data:
        oper, value = input_data.split()
        queue.appendleft(int(value))

    elif "pop_f" in input_data:

        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)

    elif "pop_b" in input_data:
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)

    elif "size" in input_data:
        print(len(queue))

    elif "empty" in input_data:
        if len(queue) > 0:
            print(0)
        else:
            print(1)

    elif "front" in input_data:
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    elif "back" in input_data:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
