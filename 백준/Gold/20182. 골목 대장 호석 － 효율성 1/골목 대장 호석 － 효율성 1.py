import sys, heapq
input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))

ans = sys.maxsize
dist = [sys.maxsize] * (n+1)
dist[a] = 0
q = []
heapq.heappush(q, (0, 0, a))
while q:
    d, val, v = heapq.heappop(q)
    if v == b and d <= c:
        ans = min(ans, val)

    for k in graph[v]:
        cost = d + k[1]
        if cost < dist[k[0]]:
            dist[k[0]] = cost
            if val < k[1]:
                heapq.heappush(q, (cost, k[1], k[0]))
            else:
                heapq.heappush(q, (cost, val, k[0]))

print(-1 if ans == sys.maxsize else ans)