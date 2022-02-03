from os import sep


year = int(input())

a = (year % 60) % 12 - 3
if a <= 0:
    a += 12

a = chr(a + 64)

b = (year % 60) % 10 + 6

if b >= 10:
    b -= 10
print(a, b, sep='')
