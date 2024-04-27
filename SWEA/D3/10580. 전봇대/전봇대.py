T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li = [tuple(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (li[i][0] > li[j][0] and li[i][1] < li[j][1]) or (li[i][0] < li[j][0] and li[i][1] > li[j][1]):
                cnt += 1
    print(f'#{test_case} {cnt}')