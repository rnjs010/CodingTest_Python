import sys
input = sys.stdin.readline
s, c = map(int, input().split())
li = [int(input()) for _ in range(s)]

l, r = 1, max(li)
ans = 0
while l <= r:
    cnt = 0
    mid = (l + r) // 2
    for i in li:
        cnt += i // mid

    if cnt >= c:
        ans = max(ans, mid)
        l = mid + 1
    elif cnt < c:
        r = mid - 1

print(sum(li) - (c * ans))