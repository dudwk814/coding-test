n = int(input())


def cursive_function(x):
    if x == 1:
        return print(x)

    print(x)

    if x % 2 == 0:
        cursive_function(x // 2)
    else:
        cursive_function(x * 3 + 1)


cursive_function(n)
