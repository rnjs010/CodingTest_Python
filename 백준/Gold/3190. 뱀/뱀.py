import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

l = int(input())
li = deque([input().rstrip().split() for _ in range(l)])

x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
time, d, nx, ny = 0, 0, 0, 0
dq = deque([(nx, ny)])
while True:
    if li and int(li[0][0]) == time:
        d += (1 if li.popleft()[1] == 'D' else -1)

    nx += x[d % 4]
    ny += y[d % 4]
    time += 1
    if nx < 0 or ny < 0 or nx >= n or ny >= n or (ny, nx) in dq:
        break

    dq.append((ny, nx))
    if graph[ny][nx] == 1:
        graph[ny][nx] = 0
    else:
        dq.popleft()

print(time)