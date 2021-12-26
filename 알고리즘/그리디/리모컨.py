current, target = map(int, input().split())

higher = max(current, target)
lower = min(current, target)
n = higher - lower
s = 0
count = 0

buttons = [10, 5, 1, -10, -5, -1]

if 7 < n % 10 < 10:  # n이 buttons 원소의 배수가 되게 해야함
    while True:
        if n % 10 == 0:
            break
        n += 1
        count += 1

if 2 < n % 10 < 5:  # n이 buttons 원소의 배수가 되게 해야함
    while True:
        if n % 5 == 0:
            break
        n += 1
        count += 1


for button in buttons:
    count += n // button
    n %= button


print(count)
