import sys, heapq
input = sys.stdin.readline

n, v, e = map(int, input().split())
a, b = map(int, input().split())
li = [*map(int, input().split())]
graph = [[] for _ in range(v+1)]
for _ in range(e):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))


def dijkstra(v, x):
    dist = [sys.maxsize] * (v+1)
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


d_a = dijkstra(v, a)
d_b = dijkstra(v, b)

ans = 0
for i in li:
    if d_a[i] == sys.maxsize: d_a[i] = -1
    if d_b[i] == sys.maxsize: d_b[i] = -1
    ans += (d_a[i] + d_b[i])

print(ans)