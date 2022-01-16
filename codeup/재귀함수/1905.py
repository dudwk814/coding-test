import sys
sys.setrecursionlimit(1000000)
n = int(input())


def recursive_function(start):
    if start == n:
        return n

    return start + recursive_function(start + 1)


print(recursive_function(1))
