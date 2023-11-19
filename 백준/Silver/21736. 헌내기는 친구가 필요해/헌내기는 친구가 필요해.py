import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            x, y = i, j
            board[i][j] == 'X'

q = deque([])
q.append((x, y))
ans = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'X':
            if board[nx][ny] == 'P':
                ans += 1
            board[nx][ny] = 'X'
            q.append((nx, ny))

print('TT' if ans == 0 else ans)
