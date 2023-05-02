import heapq
import sys
input = sys.stdin.readline
n, h, t = tuple(map(int, input().rstrip().split()))
pq = []
for _ in range(n):
    big_h = int(input().rstrip())
    heapq.heappush(pq, -big_h)

cnt = 0
for _ in range(t):
    if -pq[0] == 1:
        break
    if -pq[0] >= h:
        big = -heapq.heappop(pq)
        heapq.heappush(pq, -(big//2))
        cnt += 1
    else:
        break

if -pq[0] >= h:
    print('NO')
    print(-pq[0])
else:
    print('YES')
    print(cnt)