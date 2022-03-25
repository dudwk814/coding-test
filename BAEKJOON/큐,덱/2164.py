from collections import deque

n = [i for i in range(1, int(input()) + 1)]

queue = deque(n)

for i in range(1, len(n)):
    x = queue.popleft()
    x = queue.popleft()
    queue.append(x)

print(queue.popleft())
