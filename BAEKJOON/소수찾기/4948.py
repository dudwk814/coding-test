import sys


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return len([i for i in range(2, n) if sieve[i] == True])


while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    elif n == 1:
        print(1)
        continue
    m = n * 2

    print(prime_list(m) - prime_list(n + 1))
