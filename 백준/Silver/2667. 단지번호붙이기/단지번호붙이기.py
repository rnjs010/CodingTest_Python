import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
cnt = 0

def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return cnt
    return False

result = 0
cnt_li = []
for i in range(n):
    for j in range(n):
        a = dfs(i, j)
        if a:
            cnt_li.append(a)
            result += 1
            cnt = 0

print(result)
for i in sorted(cnt_li):
    print(i)