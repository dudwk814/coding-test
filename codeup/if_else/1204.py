# 영어 서수로 표현하기
n = int(input())

if n <= 10:
    if n == 1:
        print(n, "st", sep='')
    elif n == 2:
        print(n, "nd", sep='')
    elif n == 3:
        print(n, "rd", sep='')
    else:
        print(n, "th", sep='')
elif n <= 20:
    print(n, "th", sep='')
elif n <= 99:
    if n % 10 == 1:
        print(n, "st", sep='')
    elif n % 10 == 2:
        print(n, "nd", sep='')
    elif n % 10 == 3:
        print(n, "rd", sep='')
    else:
        print(n, "th", sep='')
