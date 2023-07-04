import sys
input = sys.stdin.readline
n, m = tuple(map(int, input().rstrip().split()))

li = [[0]*(n+1)]
for _ in range(n):
    li.append([0]+list(map(int, input().rstrip().split())))

prefix_sum = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + li[i][j]

for _ in range(m):
    x1, y1, x2, y2 = tuple(map(int, input().rstrip().split()))
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])