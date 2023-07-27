n, s = map(int, input().split())
li = [*map(int, input().split())]

left, right = 0, 0
total = 0
ans = n + 1
while True:
    if total >= s:
        ans = min(ans, right - left)
        total -= li[left]
        left += 1
    elif right == n: break
    elif total < s:
        total += li[right]
        right += 1

print(ans if ans != (n + 1) else 0)