from collections import deque
t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    queue = deque()

    importance = list(map(int, input().split()))

    for i in range(n):
        queue.append((i + 1, importance[i]))

    count = 0

    importance.sort(reverse=True)

    max_value = importance[0]

    while queue:

        no, score = queue.popleft()

        if score == max_value:
            count += 1
            if m + 1 == no:
                print(count)
                break
            max_value = importance[count]
        else:
            queue.append((no, score))
