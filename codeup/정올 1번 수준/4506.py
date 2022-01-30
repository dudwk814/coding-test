import math

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
print(math.gcd(a, b))
# print(math.lcm(a, b))
for i in range(a, a * b + 1, a):
    if i % b == 0:
        print(i)
        break
