from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v, visited):
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    
visited = [0] * (n+1)
cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i, visited)
        cnt += 1

print(cnt)
