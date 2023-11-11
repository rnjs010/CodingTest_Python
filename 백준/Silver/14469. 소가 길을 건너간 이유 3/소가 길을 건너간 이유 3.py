import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    li.append((a, b))

li.sort(key= lambda x: (x[0], x[1]))

ans = li[0][0] + li[0][1]
for i in range(1, n):
    if li[i][0] > ans:
        ans = li[i][0]
    ans += li[i][1]

print(ans)