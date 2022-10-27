import math

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    n = math.lcm(a, b)

    print(n)
