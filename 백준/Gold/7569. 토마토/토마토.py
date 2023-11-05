import sys
input = sys.stdin.readline
from collections import deque

n, m, h = map(int, input().split())
board = [[[*map(int, input().split())] for _ in range(m)] for _ in range(h)]
dx, dy, dh = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
cnt, zero = 0, 0
q= deque([])
for z in range(h):
    for i in range(m):
        for j in range(n):
            if board[z][i][j] == 1:
                q.append((z, i, j))
            if board[z][i][j] == 0:
                zero += 1

if zero == 0:
    print(0)
else:
    while q:
        z, i, j = q.popleft()
        for k in range(6):
            nx, ny, nz = i + dx[k], j + dy[k], z + dh[k]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and board[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                board[nz][nx][ny] = board[z][i][j] + 1
                cnt = board[nz][nx][ny]
                zero -= 1

    print(-1 if zero != 0 else cnt-1)