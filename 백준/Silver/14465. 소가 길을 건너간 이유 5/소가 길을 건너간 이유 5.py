import sys
input = sys.stdin.readline
n, k, b = map(int, input().split())
li = [0] * n

for _ in range(b):
    li[int(input()) - 1] = 1

ans = sum(li[0:k])
cnt = ans
for i in range(1, n-k+1):
    if li[i-1] == 1:
        cnt -= 1
    if li[i+k-1] == 1:
        cnt += 1

    ans = min(ans, cnt)

print(ans)