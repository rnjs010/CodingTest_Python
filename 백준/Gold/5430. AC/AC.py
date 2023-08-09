import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    li = input().rstrip()
    if n == 0 and 'D' in p:
        print('error')
        continue
    elif n == 0:
        dq = deque()
    else:
        dq = deque([*map(int, li[1:len(li)-1].split(','))])

    cnt = 0
    for i in p:
        if i == 'D' and dq:
            if cnt % 2 == 0:
                dq.popleft()
            else:
                dq.pop()
        elif i == 'R':
            cnt += 1
        else:
            print('error')
            break
    else:
        if cnt % 2 == 1:
            dq.reverse()
        print('[' + ','.join(map(str, dq)) + ']')