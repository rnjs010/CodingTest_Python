import heapq
import sys
input = sys.stdin.readline
n, m = tuple(map(int, input().rstrip().split()))
li = list(map(int, input().rstrip().split()))
child = list(map(int, input().rstrip().split()))
pq = []
check = 1
for i in li:
    heapq.heappush(pq, -i)

for i in child:
    p = -heapq.heappop(pq)
    if p >= i:
        heapq.heappush(pq, -p+i)
    else:
        check = 0
        break

print(check)