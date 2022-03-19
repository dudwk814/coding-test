n = int(input())
count = 1
value = 666

for i in range(667, 2666800):

    value = i

    str_value = str(value)

    if str_value.count("666") >= 1:
        count += 1

    if count == n:
        break


print(value)
