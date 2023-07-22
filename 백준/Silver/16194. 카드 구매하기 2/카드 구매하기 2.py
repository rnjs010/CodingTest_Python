n = int(input())
price = [*map(int, input().split())]
dp = [0] + price
for i in range(2, n+1):
    for j in range(1, i//2 + 1):
        if dp[i] > (dp[i-j] + dp[j]):
            dp[i] = dp[i-j] + dp[j]

print(dp[n])