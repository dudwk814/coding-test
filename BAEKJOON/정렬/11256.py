t = int(input())

for i in range(t):
    j, n = map(int, input().split())
    s = []
    for k in range(n):
        r, c = map(int, input().split())
        weigth = r * c

        s.append(weigth)

    s.sort(reverse=True)

    box = 0
    size = 0

    for value in s:
        size += value
        box += 1

        if size >= j:
            break

    print(box)
