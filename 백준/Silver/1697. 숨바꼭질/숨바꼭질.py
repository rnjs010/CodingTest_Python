import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == k:
            return visit[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and not visit[i]:
                visit[i] = visit[x] + 1
                q.append(i)


n, k = map(int, input().split())
visit = [0] * 100001
print(bfs(n))