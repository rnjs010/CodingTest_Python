T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    one_li = []
    for i in range(7):
        if li[i] == 1: one_li.append(i)
        
    ans = 1e9
    for i in one_li:
        result, idx, cnt = 0, i, 0
        while True:
            if cnt == N: break
            if li[idx % 7] == 1:
                cnt += 1
            result += 1
            idx += 1
        ans = min(ans, result)
    print(f'#{tc} {ans}')
