import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
li = sorted([*map(int, input().split())])

l, r, cnt = 0, n-1, 0
while l < r:
    t = li[l] + li[r]
    if t == m:
        l += 1
        r -= 1
        cnt += 1
    elif t < m:
        l += 1
    else:
        r -= 1

print(cnt)