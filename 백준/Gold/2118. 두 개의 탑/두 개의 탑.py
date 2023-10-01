import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]

ps = [0] * (2 * n + 1)
for i in range(2 * n):
    ps[i + 1] = ps[i] + li[i % n]

ans = 0
total, r = sum(li), 1
for l in range(2 * n):
    while r < 2 * n + 1 and ps[r] - ps[l] <= total - ps[r] + ps[l]:
        ans = max(ans, ps[r] - ps[l])
        r += 1
print(ans)