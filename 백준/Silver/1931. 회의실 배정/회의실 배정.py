import sys
input = sys.stdin.readline
n = int(input().rstrip())
li = [tuple(map(int, input().rstrip().split())) for _ in range(n)]

li.sort(key=lambda x : (x[1], x[0]))
end = li[0][1]
cnt = 1
for i in range(1, n):
    if li[i][0] >= end:
        end = li[i][1]
        cnt += 1

print(cnt)