import sys
n = int(input())
s = [0] * 21


def find_value(value):

    value = int(w[-1])

    return value


for i in range(n):
    w = sys.stdin.readline().strip()

    if not "all" in w and not "empty" in w:
        value = find_value(w[-1])

    if "add" in w:

        if s[value] == 0:
            s[value] = 1
    elif "remove" in w:

        if s[value] == 1:
            s[value] = 0
    elif "check" in w:

        if s[value] == 1:
            print(1)
        else:
            print(0)
    elif "toggle" in w:
        if s[value] == 1:
            s[value] = 0
        else:
            s[value] = 1
    elif "all" in w:
        s = [1] * 21
    elif "empty" in w:
        s = [0] * 21
