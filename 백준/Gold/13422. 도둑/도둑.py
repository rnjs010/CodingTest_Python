import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    li = [*map(int, input().split())]

    money = sum(li[0:m])
    cnt = 0
    for i in range(1, n + 1):
        if money < k:
            cnt += 1
        if n == m: break

        r = i + m - 1
        if r >= n:
            r -= n
        money -= li[i - 1]
        money += li[r]

    print(cnt)