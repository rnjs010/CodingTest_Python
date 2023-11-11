import sys
input = sys.stdin.readline

n = int(input())
li = [[*map(int, input().split())] for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            cost1 = dp[i][j - 1] if li[i][j] < li[i][j - 1] else dp[i][j - 1] + li[i][j] - li[i][j - 1] + 1
            dp[i][j] += cost1
        elif j == 0:
            cost2 = dp[i - 1][j] if li[i][j] < li[i - 1][j] else dp[i - 1][j] + li[i][j] - li[i - 1][j] + 1
            dp[i][j] += cost2
        else:
            cost1 = dp[i][j - 1] if li[i][j] < li[i][j - 1] else dp[i][j - 1] + li[i][j] - li[i][j - 1] + 1
            cost2 = dp[i - 1][j] if li[i][j] < li[i - 1][j] else dp[i - 1][j] + li[i][j] - li[i - 1][j] + 1
            dp[i][j] = min(cost1, cost2)

print(dp[n - 1][n - 1])