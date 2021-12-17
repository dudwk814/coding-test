# 이 달은 며칠까지 있을까?


y, m = map(int, input().split())

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    leapYear = True
else:
    leapYear = False

if leapYear:
    if m == 2:
        print(29)
else:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print(31)
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print(30)
    else:
        print(28)
