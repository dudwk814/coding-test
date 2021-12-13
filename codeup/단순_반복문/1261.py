# 10개의 수 중 5의 배수를 하나만 출력

a = list(map(int, input().split()))
d = []

for i in range(10):
    if a[i] % 5 == 0:
        d.append(a[i])

if len(d) == 0:
    print(0)
else:
    print(d[0])
