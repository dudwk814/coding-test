# 큰 수 비교
list = list(map(int, input().split()))

list.sort()

for i in range(len(list)):
    print(list[i], end=' ')
