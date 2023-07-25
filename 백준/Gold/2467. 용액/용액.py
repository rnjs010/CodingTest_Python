n = int(input())
li = [*map(int, input().split())]

l, r = 0, n - 1
minval = abs(li[l] + li[r])
ans = [li[l], li[r]]

while l != r:
    if minval > abs(li[l] + li[r]):
        minval = abs(li[l] + li[r])
        ans = [li[l], li[r]]
    
    if li[l] + li[r] > 0:
        r -= 1
    elif li[l] + li[r] < 0:
        l += 1
    else:
        break

print(*ans)