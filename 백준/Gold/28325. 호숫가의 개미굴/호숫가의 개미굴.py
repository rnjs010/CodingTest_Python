import sys, heapq
input = sys.stdin.readline

n = int(input())
li = [*map(int, input().split())]
check = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    if li[i-1] > 0:
        dp[i] = dp[i-1] + li[i-1]
    elif li[i-1] == 0 and check[i-1] == 0 and check[(i+1)%n] == 0:
        dp[i] = dp[i-1] + 1
        check[i] = True
    else:
        dp[i] = dp[i-1]

print(dp[n])