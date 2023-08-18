import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dfs(x, y):
    visit = [[0]*n for _ in range(n)]
    dis = [[0]*n for _ in range(n)]
    visit[x][y] = 1
    q = deque()
    q.append([x, y])
    fish = []
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and board[nx][ny] <= size:
                visit[nx][ny] = 1
                q.append([nx, ny])
                dis[nx][ny] = dis[x][y] + 1
                if 0 < board[nx][ny] < size:
                    fish.append((dis[nx][ny], nx, ny))

    return sorted(fish, key=lambda x: (x[0], x[1], x[2]))


ans, cnt, size = 0, 0, 2
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j

while True:
    li = dfs(x, y)
    if li:
        dis, nx, ny = li[0]
        ans += dis
        board[x][y], board[nx][ny] = 0, 0
        x, y = nx, ny
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
    else:
        print(ans)
        break