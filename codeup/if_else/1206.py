# 배수

a, b = map(int, input().split())

if b % a == 0:
    x = int(b / a)
    print("%d" % a + "*" + "%d" % x + "=" + "%d" % b)
elif a % b == 0:
    x = int(a / b)
    print("%d" % b + "*" + "%d" % x + "=" + "%d" % a)
else:
    print('none')
