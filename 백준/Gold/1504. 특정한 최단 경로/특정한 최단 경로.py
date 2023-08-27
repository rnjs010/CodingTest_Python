import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    dist = [sys.maxsize] * (n+1)
    dist[x] = 0
    q = []
    heapq.heappush(q, (0, x))
    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue
        for k in graph[v]:
            cost = d + k[1]
            if cost < dist[k[0]]:
                dist[k[0]] = cost
                heapq.heappush(q, (cost, k[0]))
    return dist


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
s_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

ans = min(s_dist[v1] + v1_dist[v2] + v2_dist[n], s_dist[v2] + v2_dist[v1] + v1_dist[n])
print(ans if ans < sys.maxsize else -1)