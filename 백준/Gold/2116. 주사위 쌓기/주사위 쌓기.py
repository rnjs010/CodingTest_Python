import sys
input = sys.stdin.readline
n = int(input())
li = [[*map(int, input().split())] for _ in range(n)]

dice = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
ans = []
for d in [(0, 5), (1, 3), (2, 4)]:
    for i in d:
        up, max_n = li[0][i], 0
        for m in range(6):
            if m not in d:
                max_n = max(max_n, li[0][m])
        total = max_n
        for j in range(1, n):
            max_n = 0
            for k in range(6):
                if up == li[j][k]:
                    up = li[j][dice[k]]
                    x = k
                    break
            for m in range(6):
                if m not in (x, dice[x]):
                    max_n = max(max_n, li[j][m])
            total += max_n
        ans.append(total)

print(max(ans))