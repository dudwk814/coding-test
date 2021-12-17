# 세 수 정렬하기

list = list(map(int, input().split()))

list.sort()

for i in range(len(list)):
    print(list[i], end=' ')
