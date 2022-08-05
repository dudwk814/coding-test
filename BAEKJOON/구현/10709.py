import sys

h, w = map(int, input().split())

graph = []

for i in range(h):
    array = list(input())
    graph.append(array)

for i in range(h):
    p = 0
    for j in range(w):

        if graph[i][j] == 'c':
            print(0, end=' ')
            if j != 0:
                p = j + 1
            else:
                p += 1
        elif p == 0:
            print(-1, end=' ')
        else:
            print((j + 1) - p, end=' ')

    print()
