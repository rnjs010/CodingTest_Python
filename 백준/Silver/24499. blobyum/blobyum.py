import sys
input = sys.stdin.readline
n, k = map(int, input().split())
li = [*map(int, input().split())]

ps = [0] * (n + 1)
for i in range(1, n+1):
    ps[i] = ps[i-1] + li[i-1]

if k == 1:
    print(max(li))
elif k == n:
    print(ps[-1])
else:
    val = 0
    for i in range(1, n+1):
        if i >= n - k + 2:
            val = max(val, ps[n] - ps[i-1] + ps[i+k-1-n])
        else:
            val = max(val, ps[i+k-1] - ps[i-1])

    print(val)