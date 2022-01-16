a, b = map(int, input().split())


def recursive_function(a):

    if a == b:
        if b % 2 != 0:
            return print(b)
        else:
            return
    elif a % 2 != 0:
        print(a, end=' ')
    recursive_function(a + 1)


recursive_function(a)
