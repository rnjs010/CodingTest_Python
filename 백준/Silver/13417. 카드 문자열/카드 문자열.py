from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    li = input().rstrip().split()
    dq = deque([li[0]])
    for i in range(1, n):
        f = dq[0]
        if li[i] > f:
            dq.append(li[i])
        else:
            dq.appendleft(li[i])

    print(''.join(dq))
