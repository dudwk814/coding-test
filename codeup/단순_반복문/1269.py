# 수열의 값 구하기
a, b, c, n = map(int, input().split())

for i in range(n - 1):
    a = a * b + c

print(a)
