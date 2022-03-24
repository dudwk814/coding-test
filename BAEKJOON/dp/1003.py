import sys

sys.setrecursionlimit(10000)


t = int(input())


def fibo(n):

    if n == 0:
        return dp[0]

    if n == 1:
        return dp[1]
    if n == 2:
        return dp[2]
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibo(n - 1) + fibo(n - 2)
        return dp[n]


for i in range(t):
    n = int(input())
    dp = [0] * 41
    dp[1] = 1
    dp[2] = 1
    fibo(n)

    if n == 0:
        print(1,0)
    else:
        print(dp[n - 1], dp[n])
