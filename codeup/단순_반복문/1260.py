# 3의 배수의 합

a, b = map(int, input().split())
s = 0

if a == b:
    if a % 3 == 0:
        print(a)
    else:
        print(s)
elif a < b:
    for i in range(a, b + 1):
        if i % 3 == 0:
            s += i
    print(s)
