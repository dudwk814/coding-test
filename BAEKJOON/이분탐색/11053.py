
import sys
n = int(input())
t = list(map(int, sys.stdin.readline().split()))


L = [t[0]]
for i in range(1, n):
    if t[i] > L[-1]:
        L.append(t[i])
        continue
    # μ΄λΆνμ
    l = 0
    r = len(L)-1
    m = (l+r)//2
    while l < r:
        if L[m] == t[i]:
            break
        elif L[m] > t[i]:
            r = m
        else:
            l = m+1
        m = (l+r)//2
    L[m] = t[i]
print(len(L))
