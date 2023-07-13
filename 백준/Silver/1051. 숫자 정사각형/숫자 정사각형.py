import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [*(input().rstrip() for _ in range(n))]
max_s = min(n, m)

for s in range(max_s-1, -1, -1):
    for i in range(n-s):
        for j in range(m-s):
            if li[i][j] == li[i][j+s] == li[i+s][j] == li[i+s][j+s]:
                print((s + 1)**2)
                exit()