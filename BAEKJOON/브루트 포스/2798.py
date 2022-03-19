import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())

d = list(map(int, sys.stdin.readline().split()))

combi = list(combinations(d, 3))
result = 0
for value in combi:
    if sum(value) <= m:
        result = max(result, sum(value))
print(result)
