T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    li = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(K + 1):
            V, C = li[i]
            if j < V:   # 넣을 수 없을 때
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-V] + C)
    print(f'#{tc} {dp[N][K]}')
