m = int(input())
n = int(input())
d = []


def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for i in range(m, n + 1):
    if i == 1:
        continue

    if is_prime_number(i):
        d.append(i)

if len(d) == 0:
    print(-1)
else:
    print(sum(d))
    print(min(d))
