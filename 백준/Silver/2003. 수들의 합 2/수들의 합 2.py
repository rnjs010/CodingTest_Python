n, m = map(int, input().split())
li = list(map(int, input().split()))

left = 0
right = 1
total = li[left]
cnt = 0
while left <= right:
    if total < m:
        if right == n:
            break
        total += li[right]
        right += 1
    elif total == m:
        cnt += 1
        total -= li[left]
        left += 1
    else:
        total -= li[left]
        left += 1

print(cnt)