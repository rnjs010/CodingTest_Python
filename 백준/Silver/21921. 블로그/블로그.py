import sys
input = sys.stdin.readline

n, x = map(int, input().split())
li = [*map(int, input().split())]

psum = [0] * (n+1)
for i in range(1, n+1):
    psum[i] = psum[i-1] + li[i-1]

ans, cnt = 0, 0
for i in range(x, n+1):
    if ans < psum[i] - psum[i-x]:
        ans = psum[i] - psum[i-x]
        cnt = 1
    elif ans == psum[i] - psum[i-x]:
        cnt += 1

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(cnt)