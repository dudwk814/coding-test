# # 어떤 수(n)가 입력되면 두 소수의 곱으로 나타낼 수 있으면 두 소수를 오름차순으로 출력하고,
# # 그렇지 않으면 "wrong number"를 출력
# 소인수 분해 문제

n = int(input())  # 정수 n
a = 0  # a < n을 만족하는 소수 중 가장 작은 소수
b = 0  # a * b == n을 만족하는 소수
d = 0  # 소수 판별 변수, 값이 0이면 소수
for i in range(2, n):
    if n % i == 0:
        d = 0
        a = i
        b = n / a
        if n % b == 0 and b > 1 and b % i != 0:
            if a * b == n:
                print(a, int(b))
                break
        else:
            print("wrong number")
            break
    else:
        d = 1

if n == 1 or n == 2 or d == 1:
    print("wrong number")
