n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 3
#dp[1] = 1, dp[2] = 3, dp[3] = 5, dp[4] = 11
#dp[i] = dp[i - 1] + dp[i - 2] * 2

for i in range (3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n])