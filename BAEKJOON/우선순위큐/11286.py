import heapq
import sys

n = int(sys.stdin.readline())

d = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(d) > 0:
            small_value = heapq.heappop(d)
            # if d.count(small_value) > 0:
            #     d.remove(small_value)
            print(small_value)
        else:
            print(0)
    else:
        heapq.heappush(d, x)
