n, m = map(int, input().split())
li = list(map(int, input().split()))
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