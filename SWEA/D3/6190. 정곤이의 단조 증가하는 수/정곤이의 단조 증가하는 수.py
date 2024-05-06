T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            num = li[i] * li[j]
            if num > ans:
                temp = num
                for _ in range(len(str(num))-1):
                    chk = temp % 10
                    temp //= 10
                    n_chk = temp % 10
                    if chk < n_chk:
                        break
                else:
                    ans = max(ans, num)
    ans = -1 if ans == 0 else ans
    print(f'#{tc} {ans}')