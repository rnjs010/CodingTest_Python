import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    dist[start] = 0
    while hq:
        d, now = heapq.heappop(hq)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))


v, e = map(int, input().split())
k = int(input())

dist = [int(1e9)] * (v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(k)
for i in dist[1:]:
    print('INF' if i == int(1e9) else i)