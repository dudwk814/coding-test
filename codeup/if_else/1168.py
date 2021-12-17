# 나이 계산 1
y, sex = map(int, input().split())
result = 0

y = str(y)

if len(y) == 6:
    y = y[0:2]
elif len(y) == 5:
    y = y[0]
else:
    y = 0

if sex < 3:
    result = 2012 - (1900 + int(y)) + 1
    print(result)
else:
    result = 2012 - (2000 + int(y)) + 1
    print(result)
