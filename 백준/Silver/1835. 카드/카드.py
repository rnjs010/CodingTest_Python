from collections import deque

n = int(input())
dq = deque()
for i in range(n, 0, -1):
    dq.appendleft(i)
    for _ in range(i):
        dq.appendleft(dq.pop())

print(*dq)