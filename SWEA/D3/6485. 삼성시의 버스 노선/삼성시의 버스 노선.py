T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    line = [tuple(map(int, input().split())) for _ in range(N)]
    P = int(input())
    station = [int(input()) for _ in range(P)]
    ans = [0] * P
    for a, b in line:
        for i in range(P):
            if a <= station[i] <= b:
                ans[i] += 1
    result = ' '.join(map(str, ans))
    print(f'#{test_case} {result}')