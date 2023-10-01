import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [*map(int, input().split())]

l, r = min(li), m * max(li)
ans = sys.maxsize
while l <= r:
    cnt = 0
    mid = (l + r) // 2
    for i in li:
        cnt += mid // i
    
    if cnt >= m:
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1

print(ans)