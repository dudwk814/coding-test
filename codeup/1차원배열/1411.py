# 빠진 카드
n = int(input())

list = list(range(1, n + 1))


for i in range(n - 1):
    d = int(input())

    list.remove(d)

print(list[0])
