import sys
sys.setrecursionlimit(10 ** 9)

dp = [0] * 46
dp[1] = 1
dp[2] = 1


def fibo(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1

    if dp[x] != 0:
        return dp[x]

    else:
        dp[x] = fibo(x - 1) + fibo(x - 2)
        return dp[x]


print(fibo(int(input())))
