n, m = map(int, input().split())

INF = 987654321
dp = [INF] * (m + 1)

arr = []
for i in range(n):
    arr.append(int(input()))

for i in arr:
    if m < i:
        continue
    dp[i] = 1

for i in arr:
    for j in range(i, m + 1):
        if dp[j - i] != INF:
            dp[j] = min(dp[j - i] + 1, dp[j])

if dp[m] != INF:
    print(dp[m])
else:
    print(-1)