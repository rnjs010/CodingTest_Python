import heapq
import sys
input = sys.stdin.readline
n, m, k = tuple(map(int, input().rstrip().split()))
pq = []
li = [tuple(map(int, input().rstrip().split())) for _ in range(k)]
s_li = sorted(li, key=lambda x: (x[1], x[0]))
m_val = -1
p = 0

for i in s_li:
    p += i[0]
    heapq.heappush(pq, i[0])
    if len(pq) == n:
        if m <= p:
            m_val = i[1]
            break
        else:
            p -= heapq.heappop(pq)

print(m_val)