import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [0] + [*map(int, input().split())]
ans = [1] * n
l, r, jump = 0, 0, 1

while l <= r:
    if r < n:
        r += 1

    if r == n:
        break

    if li[r] > k:
        if jump == 0:
            l += 1
            ans[l] = ans[l-1] - 1
            if li[l] > k:
                jump = 1
            else:
                r -= 1
        if jump == 1:
            jump -= 1
            ans[l] += 1
    elif li[r] <= k:
        ans[l] += 1

print(max(ans))