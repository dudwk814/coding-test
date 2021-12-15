# 삼각형 출력하기1
n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end='')
        if i == j:
            break
    print()
