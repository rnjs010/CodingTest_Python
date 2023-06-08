x, y = map(int, input().split())
start, end = 0, x
answer = x + 1
z = (y * 100) // x

while start <= end:
    mid = (start + end) // 2

    if z < ((y + mid) * 100) // (x + mid):
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(-1 if answer == (x + 1) else answer)