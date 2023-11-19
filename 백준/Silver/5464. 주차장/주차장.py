from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = [int(input()) for _ in range(n)]
use = [0] * n

w = [0] * (m+1)
for i in range(1, m+1):
    w[i] = int(input())

q = deque([])
total = 0
for _ in range(2*m):
    car = int(input())
    if car > 0:
        q.append(car)
        for i in range(n):
            if use[i] == 0:
                use[i] = q.popleft()
                break
    else:
        idx = use.index(-car)
        use[idx] = 0
        total += (w[-car] * p[idx])
        if q:
            use[idx] = q.popleft()

print(total)