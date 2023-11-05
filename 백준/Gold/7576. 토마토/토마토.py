import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cnt, zero = 0, 0
q, li = deque([]), deque([])
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            li.append((i, j))
        if board[i][j] == 0:
            zero += 1
q.append(li)

if zero == 0:
    print(0)
else:
    while len(q[0]) != 0:
        day = q.popleft()
        cnt += 1
        d = deque([])
        while day:
            i, j = day.popleft()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
                    d.append((nx, ny))
                    board[nx][ny] = 1
                    zero -= 1
        q.append(d)
        
    print(-1 if zero != 0 else cnt-1)