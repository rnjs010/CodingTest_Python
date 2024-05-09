d = {}
rev_d = {}
i, j = 1, 1
for n in range(1, 50000):
    d[n] = (i, j)
    rev_d[(i, j)] = n
    i, j = i - 1, j + 1
    if i < 1: i, j = j, 1

T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    x1, y1 = d[p]
    x2, y2 = d[q]
    print(f'#{tc} {rev_d[(x1+x2, y1+y2)]}')
