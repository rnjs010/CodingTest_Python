from itertools import combinations
t = int(input())
for _ in range(t):
    n = int(input())
    li = [*input().split()]
    ans = 100
    if n >= 33:
        print(0)
    else:
        for i in [*combinations(li, 3)]:
            cnt = 0
            for j in range(4):
                if i[0][j] != i[1][j]: cnt += 1
                if i[0][j] != i[2][j]: cnt += 1
                if i[1][j] != i[2][j]: cnt += 1
            ans = min(ans, cnt)
        print(ans)