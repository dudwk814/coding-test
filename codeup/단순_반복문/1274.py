# 소수 판별
n = int(input())
d = []
for i in range(2, n + 1):
    if n % i == 0:
        d.append(i)

if len(d) == 1:
    print("prime")
elif len(d) > 1:
    print("not prime")    