import heapq
import sys
input = sys.stdin.readline
n = int(input())
pq = []
for _ in range(n):
    i = int(input())
    heapq.heappush(pq, i)

total = 0
while len(pq) != 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    total += (a+b)
    heapq.heappush(pq, a+b)

print(total)