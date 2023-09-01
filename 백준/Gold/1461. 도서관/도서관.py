import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted([*map(int, input().split())], reverse=True)
minus, plus = [], []
for i in li:
    if i < 0: minus.append(-i)
    else: plus.append(i)

dist = []
minus.sort(reverse=True)
for i in range(len(minus) // m):
    dist.append(minus[m * i])
if len(minus) % m != 0:
    dist.append(minus[m * (len(minus) // m)])

for i in range(len(plus) // m):
    dist.append(plus[m * i])
if len(plus) % m != 0:
    dist.append(plus[m * (len(plus) // m)])

ans = 0
dist.sort()
ans = dist.pop()
ans += (sum(dist) * 2)
print(ans)