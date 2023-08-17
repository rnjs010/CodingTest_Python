import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dfs(y, x, s):
    global cnt
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == s:
                graph[ny][nx] = 0
                cnt += 1
                q.append([ny, nx])

w_total = 0
b_total = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] != 0:
            cnt = 1
            if graph[i][j] == 'W':
                graph[i][j] = 0
                dfs(i, j, 'W')
                w_total += cnt**2
            else:
                graph[i][j] = 0
                dfs(i, j, 'B')
                b_total += cnt**2

print(w_total, b_total)