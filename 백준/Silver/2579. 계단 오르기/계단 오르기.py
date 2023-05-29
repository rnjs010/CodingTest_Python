n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

dp = [0] * n
dp[0] = s[0]
if n >= 2:
    dp[1] = s[0] + s[1]
if n > 2:
    dp[2] = max(s[0] + s[2], s[1] + s[2])
    for i in range(3, n):
        dp[i] = max(s[i] + dp[i-2], s[i] + s[i-1] + dp[i-3])

print(dp[-1])