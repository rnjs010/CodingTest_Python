import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    li = [*map(int, input().split())]

    ps = [0] * (n + 1)
    for i in range(1, n+1):
        ps[i] = ps[i-1] + li[i-1]

    max_val = ps[-1]
    for i in range(2, n+1):
        for j in range(1, i+1):
            max_val = max(max_val, ps[i] - ps[j-1])

    print(max_val)