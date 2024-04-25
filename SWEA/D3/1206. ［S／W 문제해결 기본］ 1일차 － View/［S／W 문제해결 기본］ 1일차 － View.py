for test_case in range(1, 11):
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in range(2, n - 2):
        r = li[i] - max(li[i+1], li[i+2])
        l = li[i] - max(li[i-1], li[i-2])
        if r > 0 and l > 0:
            ans += min(r, l)
    print(f'#{test_case} {ans}')