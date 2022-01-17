from re import X


n = int(input())


def recursive_function(x):
    if x == 1:
        return print(x)
    if x % 2 == 0:
        recursive_function(x // 2)
    else:
        recursive_function(x * 3 + 1)
    return print(x)


recursive_function(n)
