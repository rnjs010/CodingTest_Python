import sys
input = sys.stdin.readline
m, n = map(int, input().split())
li = [*map(int, input().split())]

start = 1
end = max(li)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in li:
        cnt += (i // mid)

    if cnt >= m:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)