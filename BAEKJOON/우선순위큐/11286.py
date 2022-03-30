import heapq
import sys

n = int(sys.stdin.readline())

d = []
array = []
for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(d) == 0:
            print(0)
        else:
            abs_value, value = heapq.heappop(d)
            print(value)
    else:
        heapq.heappush(d, (abs(x), x))
