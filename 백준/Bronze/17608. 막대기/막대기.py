import sys
input = sys.stdin.readline
n = int(input())
s = [int(input()) for _ in range(n)]

cnt = 1
a = s.pop()
while s:
    v = s.pop()
    if v > a:
        a = v
        cnt += 1

print(cnt)