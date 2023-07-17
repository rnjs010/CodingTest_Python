n = int(input())
dp = [float('inf')] * 100001

dp[2], dp[4], dp[5] = 1, 2, 1
for i in range(6, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

print(-1 if dp[n] == float('inf') else dp[n])