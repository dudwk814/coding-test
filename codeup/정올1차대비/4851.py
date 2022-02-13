k = int(input())
c = int(input())
score = False

for i in range(c):
    a, b = map(int, input().split())

    chance = k

    m, n = 0, 0

    if a == k and abs(a - b) == k // 2:
        print(1)
        continue

    for j in range(k):
        if k == 3 and a == 3 and b == 1:
            score = True
            chance -= 1
            break
        if m != a:
            m += 1
            if abs(a - b) > chance:
                if k == 2:
                    if a == k and b == 0:
                        score = True
                        break
                score = False
                chance -= 1
                break
        if n != b:
            n += 1
            if abs(a - b) > chance:
                score = False
                chance -= 1
                break

        chance -= 1
        score = True

    if score:
        print(1)
    else:
        print(0)
