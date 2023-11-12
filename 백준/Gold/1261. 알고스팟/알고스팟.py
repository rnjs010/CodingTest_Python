from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[*map(int, input().rstrip())] for _ in range(m)]
visit = [[0] * n for _ in range(m)]

def dijkstra():
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    pq = []
    heappush(pq, [0, 0, 0])
    visit[0][0] = 1
    while pq:
        ans, x, y = heappop(pq)
        if x == m - 1 and y == n - 1:
            print(ans)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if board[nx][ny] == 1:
                    heappush(pq, [ans + 1, nx, ny])
                else:
                    heappush(pq, [ans, nx, ny])

dijkstra()