import sys

n, m = map(int, input().split())
dictionary = {}
for i in range(n + m):
    if i < n:
        a, b = sys.stdin.readline().split()
        b = int(b)

        if dictionary.get(a) != None:
            dictionary.update({a: dictionary.get(a) + b})
        else:
            dictionary[a] = b
    else:
        a = sys.stdin.readline().rstrip()

        if dictionary.get(a) == None:
            print(0)
        else:
            print(dictionary.get(a))
