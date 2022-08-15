import sys
n = int(input())

s = []

for i in range(n):
    score = float(sys.stdin.readline().rstrip())

    s.append(score)

    if len(s) > 7:
        s.sort()
        s.pop()

for i in range(7):
    print('{:.3f}'.format(s[i]))
