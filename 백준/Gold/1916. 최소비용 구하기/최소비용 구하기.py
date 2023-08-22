import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [sys.maxsize] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())
dist[s] = 0
hq = []
heapq.heappush(hq, (0, s))
while hq:
    d, v = heapq.heappop(hq)
    if dist[v] < d:
        continue
    for i in graph[v]:
        cost = d + i[1]
        if cost < dist[i[0]]:
            dist[i[0]] = cost
            heapq.heappush(hq, (cost, i[0]))

print(dist[e])