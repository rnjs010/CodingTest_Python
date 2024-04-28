def dfs(n, kcal, like):
    global ans
    if n == N:
        if kcal <= L:
            ans = max(ans, like)
        return

    dfs(n+1, kcal+li[n][1], like+li[n][0])
    dfs(n+1, kcal, like)


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    li = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    dfs(0, 0, 0)
    print(f'#{test_case} {ans}')