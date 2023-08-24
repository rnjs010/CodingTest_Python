import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())

dist = [sys.maxsize] * (200000)
q = []
heapq.heappush(q, (0, n))
dist[n] = 0
while q:
    d, x = heapq.heappop(q)
    if x == k:
        print(dist[x])
        break

    if dist[x] < d:
        continue
    
    for i in ((0, x*2), (1, x+1), (1, x-1)):
        if 0 <= i[1] < 200000:
            cost = d + i[0]
            if cost < dist[i[1]]:
                dist[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))