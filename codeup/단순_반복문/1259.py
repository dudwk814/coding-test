# 1부터 nㄲ지 중 짝수의 합 구하기
n = int(input())
s = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        s += i

print(s)
