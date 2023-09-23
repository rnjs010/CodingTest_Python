import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = sorted([*map(int, input().split())])

cnt = 0
if n == 0:
    print(cnt)
else:
    l, r = 0, n-1
    while l < r:
        if li[l] + li[r] >= m:
            l += 1
            r -= 1
            cnt += 1
        else:
            l += 1
    print(cnt)