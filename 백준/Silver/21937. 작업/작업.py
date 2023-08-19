import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

cnt = 0
def dfs(x):
    global cnt
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visit[i]:
                visit[i] = 1
                q.append(i)
                cnt += 1
    return cnt

print(dfs(int(input())))