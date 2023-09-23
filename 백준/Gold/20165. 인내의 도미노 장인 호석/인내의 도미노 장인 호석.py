from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
result = [['S']*m for _ in range(n)]
dd = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0) }
cnt = 0
for _ in range(r):
    x1, y1, d = input().rstrip().split()
    x1, y1 = (int(x1)-1, int(y1)-1)
    q = deque()
    if result[x1][y1] == 'S':
        cnt += 1
        result[x1][y1] = 'F'
        q.append((board[x1][y1], x1, y1))
        while q:
            l, x, y = q.popleft()
            x1, y1 = x, y
            for _ in range(l - 1):
                x1 += dd[d][0]
                y1 += dd[d][1]
                if 0 <= x1 < n and 0 <= y1 < m and result[x1][y1] == 'S':
                    cnt += 1
                    result[x1][y1] = 'F'
                    q.append((board[x1][y1], x1, y1))

    x2, y2 = map(int, input().split())
    result[x2-1][y2-1] = 'S'

print(cnt)
for i in result:
    print(*i)