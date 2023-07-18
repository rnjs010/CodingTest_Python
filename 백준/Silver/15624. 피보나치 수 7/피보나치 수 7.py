n = int(input())
dp = [0, 1]

if n in [0, 1]:
    print(dp[n])
else:
    for i in range(2, n+1):
        dp = [dp[1], (dp[0] + dp[1]) % 1000000007]

    print(dp[1])