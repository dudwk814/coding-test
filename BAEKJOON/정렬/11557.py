t = int(input())

for i in range(t):
    s = []
    n = int(input())

    for j in range(n):
        name, score = input().split()
        score = int(score)

        s.append((name, score))

    s.sort(key=lambda x: -x[1])

    print(s[0][0])
