n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, num):
    if num == 4:
        print(1)
        exit()
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, num + 1)
            visited[i] = 0

visited = [0] * n
for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0
else:
    print(0)