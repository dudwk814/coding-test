n = int(input())
s = [i for i in range(1, n + 1)]

for i in range(n):
    print(s[0], end=' ')

    if i != n - 1:
        s.remove(s[0])
        s.append(s[0])
        s.remove(s[0])
