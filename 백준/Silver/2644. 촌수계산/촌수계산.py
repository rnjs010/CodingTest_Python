import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque([x])
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                q.append(i)

visited = [0] * (n + 1)
bfs(s)
print(visited[e] if visited[e] > 0 else -1)