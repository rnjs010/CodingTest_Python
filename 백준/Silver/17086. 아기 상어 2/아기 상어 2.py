import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]
def dfs(x, y):
    li = []
    visit = [[0]*m for _ in range(n)]
    dis = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append([nx, ny])
                dis[nx][ny] = dis[x][y] + 1
                if board[nx][ny] == 1:
                    li.append(dis[nx][ny])
    return min(li)

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            ans = max(ans, dfs(i, j))

print(ans)