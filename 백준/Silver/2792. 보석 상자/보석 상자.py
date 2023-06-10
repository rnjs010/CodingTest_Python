import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
li = [int(input()) for _ in range(m)]

start, end = 1, max(li)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in li:
        if i > mid:
            cnt += math.ceil(i / mid)
        else:
            cnt += 1
    
    if cnt > n:
        start = mid + 1
    else:
        end = mid - 1

print(start)