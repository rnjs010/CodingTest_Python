import sys, heapq
input = sys.stdin.readline

num = 1
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while True:
    n = int(input())
    if n == 0: break
    graph = [[*map(int, input().split())] for _ in range(n)]
    dist = [[sys.maxsize] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = graph[0][0]
    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                cost = d + graph[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(f'Problem {num}: {dist[n-1][n-1]}')
    num += 1