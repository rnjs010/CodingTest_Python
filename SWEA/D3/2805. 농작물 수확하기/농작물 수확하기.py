T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = [list(map(int, list(input()))) for _ in range(N)]
    mid = N // 2
    ans = sum(li[mid])
    for i in range(1, mid+1):
        ans += sum(li[mid + i][i:N - i])
        ans += sum(li[mid - i][i:N - i])
    print(f'#{tc} {ans}')
