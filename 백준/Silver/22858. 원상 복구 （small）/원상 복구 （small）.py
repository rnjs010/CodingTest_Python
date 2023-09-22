import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = [0] + [*map(int, input().split())]
d = [0] + [*map(int, input().split())]

p, temp = [i for i in d], [i for i in d]

for _ in range(k-1):
    for i in range(1, n+1):
        p[i] = temp[d[i]]

    temp = [i for i in p]

ans = [0] * (n+1)
for i in range(1, n+1):
    ans[p[i]] = s[i]

print(*ans[1:])