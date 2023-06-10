import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]

start, end = max(li), sum(li)
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    total = 0
    for i in li:
        total += i
        if total > mid:
            total = i
            cnt += 1
    
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)