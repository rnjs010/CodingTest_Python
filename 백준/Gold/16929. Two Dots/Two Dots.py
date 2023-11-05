import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = False
def dfs(graph, i, j, visited, cnt, start_i, start_j):
    global ans
    if ans: return

    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == graph[i][j]:
            if cnt >= 4 and nx == start_i and ny == start_j:
                ans = True
                return
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(graph, nx, ny, visited, cnt+1, start_i, start_j)
                visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        visited[i][j] = True
        dfs(board, i, j, visited, 1, i, j)
        if ans:
            print("Yes")
            exit()
print('No')