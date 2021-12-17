# 만능 휴지통
n = int(input())

list = []
temp = 0

if n >= 10:
    for i in range(2):
        if i == 0:
            list.append(n // 10)  # n의 10자리 숫자는 n을 10로 나눈 몫이다.

        else:
            list.append(n % 10)  # n의 1자리 숫자는 n을 10으로 나눈 나머지이다.

    temp = list[0]
    list[0] = list[1]
    list[1] = temp
    temp = 0

    result = ((list[0] * 10) + list[1]) * 2

    if result > 100:
        result = result % 100

    print(result)

    if result <= 50:
        print('GOOD')
    else:
        print('OH MY GOD')
else:
    result = (n * 10) * 2

    if result > 100:
        result = result % 100

    print(result)

    if result <= 50:
        print('GOOD')
    else:
        print('OH MY GOD')
