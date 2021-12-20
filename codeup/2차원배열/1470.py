# 2차원 배열 지그재그 채우기 2-3

n = int(input())
d = []
k = 0
for i in range(n):
    d.append([])
    for j in range(n):
        if i == 0:
            k += 1
            d[i].append(k)

        elif i % 2 != 0:
            if j == 0:
                k += n
                d[i].append(k)
            else:
                k -= 1
                d[i].append(k)

        else:
            if j == 0:
                k += n
                d[i].append(k)
            else:
                k += 1
                d[i].append(k)

for i in range(n):
    for j in range(n):
        print(d[j][i], end=' ')
    print()
