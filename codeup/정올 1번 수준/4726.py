n, k = map(int, input().split())
dp = [0] * 100000
score = list(map(int, input().split()))

dp[0] = score[0]

for i in range(1, k):
    dp[i] = dp[i - 1] + score[i]


max_value = dp[k - 1]

for i in range(k, n):
    dp[i] = dp[i - 1] - score[i - k] + score[i]
    max_value = max(max_value, dp[i])

print(max_value)
