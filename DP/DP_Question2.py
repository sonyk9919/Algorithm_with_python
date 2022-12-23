n = int(input())
arr = list(map(int, input().split()))


dp = [0] * (n)
# dp[0] = arr[0]
# dp[1] = max(arr[0], arr[1])
# dp[2] = max(dp[0] + arr[2], arr[1])
# dp[3] = max(dp[1] + arr[3], dp[2])
# ...
# dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, n):
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])

print(dp[n - 1])
