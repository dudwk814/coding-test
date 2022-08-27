s = input()
n = int(input())


count = 0
for i in range(n):
    w = input()
    w = w + w

    if s in w:
        count += 1


print(count)
