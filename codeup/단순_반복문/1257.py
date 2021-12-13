# 두 수 사이의 홀수 출력하기
a, b = map(int, input().split())

if a == b:
    if a % 2 != 0:
        print(a)
elif a < b:
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=' ')
