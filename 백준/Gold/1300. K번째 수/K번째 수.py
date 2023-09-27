n = int(input())
k = int(input())

l, r = 1, n*n
while l <= r:
    mid = (l + r) // 2
    t = 0
    for i in range(1, n+1):
        t += min(mid // i, n)
    
    if t >= k:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)