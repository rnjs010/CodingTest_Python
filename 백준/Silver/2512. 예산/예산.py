import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
m = int(input())
start, end = 0, max(li)
total = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in li:
        total += (mid if i > mid else i)
    
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)