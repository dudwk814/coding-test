a = int(input())
s = 0

for i in range(1, a + 1):
    s += i

    if s >= a:
        print(i)
        break
