n = int(input())
d = [0] * 100


def recurcive_function(x):
    if x == 1:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = x * recurcive_function(x - 1)
    return d[x]


print(recurcive_function(n))
