# 팩토리얼 계산
n = int(input())
for i in range(n - 1, 0, -1):
    n = n * i

print(n)
