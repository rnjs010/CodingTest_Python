import sys, heapq
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))

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


d_a = dijkstra(a)
d_b = dijkstra(b)
d_c = dijkstra(c)

max_d, ans = 0, 1
for i in range(1, n+1):
    min_d = min(d_a[i], d_b[i], d_c[i])
    if max_d < min_d:
        max_d, ans = min_d, i

print(ans)