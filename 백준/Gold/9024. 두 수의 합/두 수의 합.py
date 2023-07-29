import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    li = sorted([*map(int, input().split())])
    l, r = 0, n - 1
    cnt = 0
    val = sys.maxsize
    while l < r:
        s = li[l] + li[r]
        if val > abs(k - s):
            val = abs(k - s)
            cnt = 1
        elif val == abs(k - s): cnt += 1

        if s < k: l += 1
        elif s > k: r -= 1
        else:
            l += 1
            r -= 1
    
    print(cnt)