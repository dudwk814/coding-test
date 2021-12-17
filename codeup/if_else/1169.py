# 나이 계산 2
age = int(input())

y = 2012 - age + 1

result = y % 100

if y < 2000:
    print(result, 1)
else:
    print(result, 3)
