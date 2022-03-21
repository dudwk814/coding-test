import sys
from collections import Counter

n = int(sys.stdin.readline())

d = []

for i in range(n):
    d.append(int(sys.stdin.readline()))

d.sort()
cnt = Counter(d)
cnt = cnt.most_common()

cnt.sort(key=lambda x: (-x[1], x[0]))


print(round(sum(d) / n))
print(d[len(d) // 2])
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(d) - min(d))
