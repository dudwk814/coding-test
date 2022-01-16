n = int(input())
d = [0] * 201


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = (fibo(x - 1) + fibo(x - 2)) % 10009
    return d[x]


print(fibo(n))
