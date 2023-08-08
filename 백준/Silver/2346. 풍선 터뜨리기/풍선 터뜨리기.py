from collections import deque

n = int(input())
li = [*map(int, input().split())]
dq = deque()
for i in range(n):
    dq.append((i+1, li[i]))

num, cnt = dq.popleft()
ans = [num]
while dq:
    if cnt > 0:
        for _ in range(cnt-1):
            dq.append(dq.popleft())
        num, cnt = dq.popleft()
        ans.append(num)
    else:
        for _ in range(abs(cnt)-1):
            dq.appendleft(dq.pop())
        num, cnt = dq.pop()
        ans.append(num)

print(*ans)