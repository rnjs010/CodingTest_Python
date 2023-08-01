import sys
input = sys.stdin.readline
n, k = map(int, input().split())
li = [*map(int, input().split())]

left, right = 0, sum(li)
ans = 0
while left <= right:
    mid = (left + right) // 2
    total, g = 0, 0

    for i in li:
        total += i
        if total >= mid:
            total = 0
            g += 1

    if g >= k:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)