n = int(input())


def recursive_function(x):

    if x == n:
        print('*'*n)
        return
    print('*'*x)

    recursive_function(x + 1)


recursive_function(1)
