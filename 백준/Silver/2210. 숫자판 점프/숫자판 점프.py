import sys
input = sys.stdin.readline

board = [[*map(int, input().split())] for _ in range(5)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = []
def dfs(graph, i, j, depth, s):
    if(depth == 5):
        ans.append(''.join(s))
        return

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(graph, nx, ny, depth+1, s+str(graph[nx][ny]))

for i in range(5):
    for j in range(5):
        dfs(board, i, j, 0, ''+str(board[i][j]))

print(len(set(ans)))