n = int(input())

dp = [1, 1, 1]
for i in range(3, n):
    dp += [dp[i - 1] + dp[i - 3]]

print(dp[n - 1])