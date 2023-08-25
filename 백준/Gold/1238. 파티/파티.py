import sys, heapq
input = sys.stdin.readline

def dijkstra(graph, dist):
    q = []
    heapq.heappush(q, (0, x))
    while q:
        d, k = heapq.heappop(q)

        if dist[k] < d:
            continue
        
        for i in graph[k]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph1[a].append((b, c))
    graph2[b].append((a, c))

dist1 = [sys.maxsize] * (n+1)
dist2 = [sys.maxsize] * (n+1)
dist1[x], dist2[x] = 0, 0
dijkstra(graph1, dist1)
dijkstra(graph2, dist2)

ans = 0
for i in range(1, n+1):
    ans = max(ans, dist1[i] + dist2[i])

print(ans)