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


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

j, s = map(int, input().split())
j_dist = dijkstra(j)
s_dist = dijkstra(s)

ans = []
for i in range(1, n+1):
    flag = 1
    if i == j or i == s: continue
    if j_dist[i] > s_dist[i]: flag = 0
    ans.append((j_dist[i] + s_dist[i], j_dist[i], i, flag))

li = sorted(ans, key= lambda x: (x[0], x[1], x[2], -x[3]))
ans = 0
for i in li:
    if i[0] < sys.maxsize and i[0] == li[0][0] and i[3] == 1:
        ans = i[2]
        break

print(-1 if ans == 0 else ans)