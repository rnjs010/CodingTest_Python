from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
r = 1
ans = 1
while True:
    visit = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and board[i][j] > r:
                cnt += 1
                visit[i][j] = 1
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and board[nx][ny] > r:
                            visit[nx][ny] = 1
                            q.append([nx, ny])
    if cnt == 0:
        break
    r += 1
    ans = max(ans, cnt)

print(ans)