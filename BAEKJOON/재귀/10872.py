n = int(input())


def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


if n == 0:
    print(1)
else:
    print(factorial(n))
