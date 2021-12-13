a, b = input().split()

a = ord(a)
b = ord(b)

for i in range(a, b + 1):
    print(chr(i), end=' ')
