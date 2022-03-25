from collections import deque


n, m = map(int, input().split())

queue = deque()
d = []

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(m - 1):
        queue.append(queue.popleft())

    d.append(queue.popleft())

print("<", end="")
for i in range(len(d) - 1):
    print(d[i], end=', ')
print(d[-1], end="")
print(">")
