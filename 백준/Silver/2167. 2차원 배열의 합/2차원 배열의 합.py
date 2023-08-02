import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [[*map(int, input().split())] for _ in range(n)]

ps = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + li[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(ps[x][y] - ps[x][j-1] - ps[i-1][y] + ps[i-1][j-1])