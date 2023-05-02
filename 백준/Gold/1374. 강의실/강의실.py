import heapq
import sys
input = sys.stdin.readline
n = int(input().rstrip())
li = []
for _ in range(n):
    a, b, c = tuple(map(int, input().rstrip().split()))
    li.append((b, c))

li.sort()
pq = []
heapq.heappush(pq, li[0][1])
for i in range(1, n):
    if pq[0] > li[i][0]:
        heapq.heappush(pq, li[i][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, li[i][1])

print(len(pq))