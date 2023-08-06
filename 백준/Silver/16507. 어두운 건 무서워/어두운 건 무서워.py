import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
li = [[*map(int, input().split())] for _ in range(r)]
ps = [[0]*(c+1) for _ in range(r+1)]
for i in range(1, r+1):
    for j in range(1, c+1):
        ps[i][j] = ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1] + li[i-1][j-1]

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print((ps[x2][y2] - ps[x2][y1-1] - ps[x1-1][y2] + ps[x1-1][y1-1]) // ((x2-x1+1)*(y2-y1+1)))