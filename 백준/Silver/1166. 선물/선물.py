n, l, w, h = map(int, input().split())
left, right = 0, min(l, w, h)
for _ in range(100):
    mid = (left + right) / 2
    if ((l // mid) * (w // mid) * (h // mid)) >= n:
        left = mid
    else:
        right = mid

print(right)