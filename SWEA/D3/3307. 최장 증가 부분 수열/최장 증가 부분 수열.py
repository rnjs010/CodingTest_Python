T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if li[i] > li[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f'#{test_case} {max(dp)}')