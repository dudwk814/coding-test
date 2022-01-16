n = int(input())


def recursive_function(start):

    if start == n:
        return print(n)

    print(start)
    recursive_function(start + 1)


recursive_function(1)
