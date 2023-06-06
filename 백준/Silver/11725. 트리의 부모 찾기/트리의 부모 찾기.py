import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
graph = [[] for _ in range(t+1)]
for _ in range(t-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = v

visited = [0] * (t + 1)
bfs(graph, 1, visited)
for i in visited[2:]:
    print(i)