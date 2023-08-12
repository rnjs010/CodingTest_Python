import heapq as hq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    pq = [*map(int, input().split())]
    hq.heapify(pq)
    total = 1
    while len(pq) > 1:
        e = hq.heappop(pq) * hq.heappop(pq)
        hq.heappush(pq, e)
        total *= e
    print(total % 1000000007)